from sheets import get_sheet
from enum import Enum, auto

uc_data = get_sheet('1IDfClme9QDOyW_P_3Gs4HiDlI6ZsblvmkH5Y3mJAejo', 'B2:N1000').get('values')

class Student:
    class Gender(Enum):
        MALE = auto()
        FEMALE = auto()
        OTHER = auto()

    def __init__(self, schools=None, top=None, gender=None, race=None, resident=None, major=None, income=None, sat=None, act=None, wgpa=None, gpa=None, apib=None, sleep=None):
        self.schools = schools
        self.top = top #None if non-UC
        self.gender = gender
        self.race = race
        self.resident = resident
        self.major = major
        self.income = income
        self.sat = sat
        self.act = act
        self.wgpa = wgpa
        self.gpa = gpa
        self.apib = apib
        self.sleep = sleep

students = []
for row in uc_data:
    schools = row[0].split(", ")
    top = row[1] if row[1].startswith("UC") else None
    if row[2] == "Male":
        gender = Student.Gender.MALE
    elif row[2] == "Female":
        gender = Student.Gender.FEMALE
    else:
        gender = Student.Gender.OTHER
    race = row[3]
    resident = True if row[4] == "Yes" else False
    major = row[5]
    income = row[6]
    sat = int(row[7]) if row[7] else None
    act = int(row[8]) if row[8] else None
    wgpa = float(row[9]) if row[9] else None
    gpa = float(row[10]) if row[10] else None
    apib = int(row[11])
    if row[12].startswith("less"):
        sleep = 3
    elif row[12].startswith("over"):
        sleep = 9
    else:
        sleep_split = row[12].split(" ")[0].split("-")
        sleep = (int(sleep_split[0]) + int(sleep_split[1]))/2

    students.append(Student(
        schools=schools,
        top=top,
        gender=gender,
        race=race,
        resident=resident,
        major=major,
        income=income,
        sat=sat,
        act=act,
        wgpa=wgpa,
        gpa=gpa,
        apib=apib,
        sleep=sleep
    ))



if __name__ == '__main__':
    for s in students:
        print(s.gender)
    pass
