import requests
import http
import os
import json

post_url = "https://pastebin.com/post.php"
with open(os.path.join(os.path.dirname(__file__), 'credentials' + os.sep + 'creds.json')) as jf:
    creds = json.load(jf)

lang = {
    "Python":"python",
    "Java":"java",
    "AppleScript":"applescript",
    "JavaScript":"javascript"
}

#


# key_payload = {
#     "api_dev_key":creds['dev_key'],
#     "api_user_name":creds['username'],
#     "api_user_password":creds['password']
# }

# user_key = requests.post("https://pastebin.com/api/api_login.php", key_payload).text
def make_paste(content, name, language):
    payload = {
        "api_dev_key": creds['dev_key'],
        "api_user_key": creds['user_key'],
        "api_paste_name": name,
        "api_paste_code": content,
        "api_paste_format": lang[language],
        "api_paste_private": "0",
        "api_paste_expire_date": "N",
        "api_option": "paste",
    }

    return requests.post(post_url, payload)

if __name__ == "__main__":
    print(make_paste("OWO", "UWU", "Python").text)
    pass