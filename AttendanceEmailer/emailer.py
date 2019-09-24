from googleapi import get_sheet, write_sheet, make_token
from students import students
from datetime import datetime

sheet_id = "1c7OG7u6LyVL7WMgibuKIVEylFxba2oyPzOwJD20uDfE"
tab_id = "1773382367"

class StudentAttendance:
    school_start = datetime.strptime("8:30:00", "%H:%M:%S")
    school_end = datetime.strptime("15:30:00", "%H:%M:%S")

    def __init__(self, email, attending=True, arrive=school_start, depart=school_end):
        self.email = email
        self.name = students[email]
        self.attending = attending
        self.arrive = arrive
        self.depart = depart

def get_relevant_students():
    data = get_sheet(sheet_id, "B2:E100").get('values')
    entries = []
    encountered = []

    if data:
        for n in reversed(data):
            if not n[0] in students or n[0] in encountered:
                continue
            else:
                encountered.append(n[0])
                if n[3] == "Yes":
                    if len(n[1]) > 0:
                        n[1] = datetime.strptime(n[1], "%I:%M:%S %p")

                        if StudentAttendance.school_start > n[1]:
                            n[1] = StudentAttendance.school_start
                        elif n[1] > StudentAttendance.school_end:
                            n[1] = StudentAttendance.school_end
                    else: n[1] = StudentAttendance.school_start

                    if len(n[2]) > 0:
                        n[2] = datetime.strptime(n[2], "%I:%M:%S %p")
                        if n[2] > StudentAttendance.school_end:
                            n[2] = StudentAttendance.school_end

                        if n[1] >= n[2]:
                            continue
                    else: n[2] = StudentAttendance.school_end
                    attend = True
                else:
                    attend = False
                entries.append(StudentAttendance(email=n[0], attending=attend, arrive=n[1], depart=n[2]))
    return entries

if __name__ == '__main__':
    relevant_students = get_relevant_students()
    for student in relevant_students:
        if student.attending: print(f"{student.name} is attending school, Coming: {student.arrive.time()}, Leaving: {student.depart.time()}")
        else: print(f"{student.name} is not attending school")
    write_sheet(sheet_id, "", mode="ROWS", remove=[0, 200], tab_id=tab_id)
















