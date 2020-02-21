 #!/usr/local/bin/python3.7
import json
import urllib.request
import os
from subprocess import Popen, PIPE
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from enum import Enum
import re


class Group(Enum):
    STUDENTS = ("Students", 1)
    HOUSEHOLDS = ("Households", 2)
    STAFF = ("Staff", 4)
    PK3 = ("Pre-K3", 5)
    PK4 = ("Pre-K4", 6)
    KG = ("Kindergarten", 7)
    ONE = ("Grade 1", 8)
    TWO = ("Grade 2", 9)
    THREE = ("Grade 3", 10)
    FOUR = ("Grade 4", 11)
    FIVE = ("Grade 5", 12)
    SIX = ("Grade 6", 13)
    SEVEN = ("Grade 7", 14)
    EIGHT = ("Grade 8", 15)
    NINE = ("Grade 9", 16)
    TEN = ("Grade 10", 17)
    ELEVEN = ("Grade 11", 18)
    TWELVE = ("Grade 12", 19)
    #20-34 = Households

    def __init__(self, title, directory):
        self.title = title
        self.directory = directory

def browser_load(group):
    with open(os.path.join(os.path.dirname(__file__), "credentials", "creds.json"), "r+") as jf:
        creds = json.load(jf)
    b = webdriver.Chrome()
    b.get(f"https://portals.veracross.eu/asb/student/directory/{group.directory}")

    b.find_element_by_id("username").send_keys(creds['username'])
    b.find_element_by_id("password").send_keys(creds['password'])
    b.find_element_by_id("recaptcha").click()
    b.implicitly_wait(2)

    while True:
       try:
           b.find_element_by_class_name("DirectoryEntries_LoadMoreEntriesButton").click()
       except:
           break
    if not os.path.isdir(os.path.join(os.path.dirname(__file__), "data", group.name)):
        os.mkdir(os.path.join(os.path.dirname(__file__), "data", group.name))
    for entry in b.find_elements_by_class_name("directory-Entry"):
        image_url = entry.find_element_by_class_name("directory-Entry_PersonPhoto--square").get_attribute("style").split('url("')[1][:-3]
        student_name = entry.find_element_by_class_name("directory-Entry_Title").text
        student_name = re.sub("(\(.*?\))", "", student_name).replace("  ", " ")
        urllib.request.urlretrieve(image_url, os.path.join(os.path.dirname(__file__), "data", group.name, f"{student_name}.jpg"))
        print(f"Added {student_name} to {os.path.join(os.path.dirname(__file__), 'data', group.name)}")
browser_load(Group.ELEVEN)

def load_students():
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),'students.json')) as jf:
        people = json.load(jf)


    for person in people:
        count = 1
        prepend = ""

        if person["grade"].startswith("Grade "):
            prepend = person["grade"][6:]+"-"
        elif person["grade"] == "Pre-K3":
            prepend = "PK3-"
        elif person['grade'] == "Pre-K4":
            prepend = "PK4-"
        elif person['grade'] == 'Kindergarten':
            prepend = 'KG-'

        if len(person["image"]) > 0:
            urllib.request.urlretrieve(person["image"], 'students' + os.sep + prepend + person['name'].replace("/", "") + ".jpg")
            print("Downloaded photo for " + person["name"] + " [" + str(count) + "/" + str(len(people)) + "]")
        else:
            print("No photo present for " + person["name"] + " [" + str(count) + "/" + str(len(people)) + "]")
        count+=1
def load_staff():
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),'staff.json')) as jf:
        people = json.load(jf)

    count = 1
    for person in people:
        if len(person['image']) > 0:
            urllib.request.urlretrieve(person["image"], 'staff' + os.sep + person['name'].replace("/", "") + ".jpg")
            print("Downloaded photo for " + person["name"] + " [" + str(count) + "/" + str(len(people)) + "]")
        else:
            print("No photo present for " + person["name"] + " [" + str(count) + "/" + str(len(people)) + "]")
        count+=1

def get_student_count(grade):
    count = 0
    grade = get_grade(grade)

    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),'students.json')) as jf:
        students = json.load(jf)
    for student in students:
        if student['grade'] == grade:
            count += 1
    return count

def get_grade(s):
    if s.isdigit() and 13 > int(s) > 0:
        return "Grade " + str(s)
    elif s.startswith("Grade ") and 13 > int(s.split(" ")[1]) > 0:
        return s
    elif s == "KG" or s == "Kindergarten":
        return "Kindergarten"
    elif s == "PK3" or s == "Pre-K3":
        return "Pre-K3"
    elif s == "PK4" or s == "Pre-K4":
        return "Pre-K4"
    else:
        raise NotImplementedError('The entered grade is not an option or accepted shorthand!', s)


def setup_applescript(script):
    p = Popen(['osascript'], stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    stdout, stderr = p.communicate(script)

    return {
        "output": stdout,
        "error": stderr,
        "code": p.returncode
    }

def trigger_script():
    trigger_dialog = '''
        tell application "System Events"
            set retVal to display dialog "Input a Grade" default answer ""
        end tell'''

    show_results = '''
        tell application "System Events"
            display alert "{0}"
        end tell
    '''

    td = setup_applescript(trigger_dialog)

    if td['code'] == 0:
        studentCount = get_student_count(td['output'][34:].strip())
        setup_applescript(show_results.format(get_grade(td['output'][34:].strip()) + " has " + str(studentCount) + " students."))

# if __name__ == "__main__":
#     # trigger_script()
#     load_students()