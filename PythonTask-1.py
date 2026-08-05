"""Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.
"""




import re

# Dictionary to store student marks
student_marks = {
    "Punisher": 85,
    "Michelle": 92,
    "Gwen": 95,
    "Ned": 88,
    "Peter": 90

}

# Ask the user to input a student's name
name = input("Enter the student's name: ")

found = False
# Search for the student's name in the dictionary (case-insensitive)
for student in student_marks:
    if re.search("^" + name + "$", student, re.IGNORECASE):
        print(f"{student}'s marks: {student_marks[student]}")
        found = True
        break
#if the student's name is not found, display an appropriate message
if not found:
    print("Student not found.")
