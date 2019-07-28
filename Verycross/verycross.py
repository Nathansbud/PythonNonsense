import json
import urllib.request
from os import sep

def load_students():
    with open('students.json') as jf:
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
            urllib.request.urlretrieve(person["image"], 'students' + sep + prepend + person['name'].replace("/", "") + ".jpg")
            print("Downloaded photo for " + person["name"] + " [" + str(count) + "/" + str(len(people)) + "]")
        else:
            print("No photo present for " + person["name"] + " [" + str(count) + "/" + str(len(people)) + "]")
        count+=1

def load_staff():
    with open('staff.json') as jf:
        people = json.load(jf)

    count = 1
    for person in people:
        if len(person['image']) > 0:
            urllib.request.urlretrieve(person["image"], 'staff' + sep + person['name'].replace("/", "") + ".jpg")
            print("Downloaded photo for " + person["name"] + " [" + str(count) + "/" + str(len(people)) + "]")
        else:
            print("No photo present for " + person["name"] + " [" + str(count) + "/" + str(len(people)) + "]")
        count+=1

if __name__ == "__main__":
    load_staff()
    pass
