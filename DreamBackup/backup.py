#!/usr/local/bin/python3.7

import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from subprocess import Popen, PIPE
import re
import difflib

notes_doc = '1eVzxFeJaiTbvVvfxfNyJxdgjUqLMVnUwhDE4b0cbukw'

def call_applescript(script):
    p = Popen(['osascript'], stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    stdout, stderr = p.communicate(script)

    return {
            "output": stdout,
            "error": stderr,
            "code": p.returncode
        }

def applescript_get_note(note_name):
    applescript = f'''tell application "Notes"
	set noteFolder to notes of folder "Notes"
	set theNote to ""
	
	repeat with eachNote in noteFolder
		if name of eachNote is "{note_name}" then
			set theNote to eachNote
			exit repeat
		end if
	end repeat
	
	set content to (body of theNote)
end tell'''
    return call_applescript(applescript)

def format_list(text):
    substr = text
    indices = []
    strings = []

    while True:
        matched = re.search('<li>(.*?)</li>', substr)
        if not matched:
            break
        else:
            indices.append((matched.start() + (len(text) - len(substr)), matched.end() + (len(text) - len(substr))))
            substr = substr[matched.end():]
    for elem in indices:
        strings.append(text[elem[0]:elem[1]][4:-5]) #4:-5 is the Mli and /li length
    return strings


def make_token(scope, cred_name):
    creds = None

    token_path = os.path.join(os.path.dirname(__file__), "creds" + os.sep + cred_name + "_token.pickle")
    cred_path = os.path.join(os.path.dirname(__file__), "creds" + os.sep + cred_name + ".json")

    if os.path.exists(token_path):
        with open(token_path, 'rb') as token:
            creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                cred_path, scope)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(token_path, 'wb') as token:
            pickle.dump(creds, token)

    return creds


def get_document(): #Wholesale stolen from Google examples :)
    SCOPES = ['https://www.googleapis.com/auth/documents.readonly']
    docs_token = make_token(scope=SCOPES, cred_name="docs")
    service = build('docs', 'v1', credentials=docs_token)
    return service.documents().get(documentId=notes_doc).execute()

def write_document(doc_id, content):
    old_path = os.path.join(os.path.dirname(__file__), "data" + os.sep +"old.txt")

    post_list = "\n".join(content)
    with open(old_path, 'r+') as old_text:
        old_list = [line.strip("\n") for line in old_text.readlines()]
    if [line for line in difflib.context_diff(content, old_list)]:
        print("Found diff!")
        doc_end = [paragraph['endIndex'] for paragraph in get_document()['body']['content'] if 'endIndex' in paragraph][-1]

        requests = [
            {
                'deleteContentRange': {
                    'range': {
                        'startIndex': 1,
                        'endIndex': doc_end - 1,
                    }

                }
            },
            {
                'insertText': {
                    'location': {
                        'index': 1,
                    },
                    'text':"\n".join(content)
                }
            }, {
                'createParagraphBullets': {
                    'range': {
                        'startIndex': 1,
                        'endIndex': len(post_list)
                    },
                    "bulletPreset": "BULLET_ARROW_DIAMOND_DISC"
                }
            }
        ]
        SCOPES = ['https://www.googleapis.com/auth/documents']
        docs_token = make_token(scope=SCOPES, cred_name="docs")
        service = build('docs', 'v1', credentials=docs_token)
        result = service.documents().batchUpdate(documentId=doc_id, body={'requests': requests}).execute()
        with open(old_path, 'w+') as write_to:
            write_to.write(post_list)
    else:
        print("No difference!")

if __name__ == '__main__':
    write_document(notes_doc, format_list(applescript_get_note('Dream Log')['output']))
