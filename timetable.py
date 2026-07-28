import random

days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
]
subjects = [
    "Math",
    "Physics",
    "Chemistry",
    "English",
    "Biology",
    "Computer Science"
]
random.shuffle(subjects)
timetable = {}
for i in range(len(days)):
    timetable[days[i]] = subjects[i]
print("=" * 30)
print("   SCHOOL TIMETABLE")
print("=" * 30)
for day in timetable:
    print(f"{day:<12}: {timetable[day]}")
file = open("timetable.txt", "w")
file.write("SCHOOL TIMETABLE\n")
file.write("=" * 30 + "\n")
for day in timetable:
    file.write(f"{day:<12}: {timetable[day]}\n")
file.close()
print("\nTimetable saved as timetable.txt")