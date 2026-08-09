"""
Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student's name is not found, display an appropriate message.
"""


#Dictonary of student_marks with student name as key and marks as values
student_marks = {
    "peter": 85,
    "jean": 90,
    "mary": 78,
    "ned": 92,
    "frank": 88
}
<<<<<<< HEAD

name = input("Enter the student's name: ")
=======
# Ask the user for input
name = input("Enter the student's name: ").lower()
>>>>>>> b944693b0879ffee7c33dfbea00f13e19b925359

if name in student_marks:
    name == student_marks[name]
    print(f"{name}'s marks: {student_marks[name]}")

else:
    print("Student not found. Try Again")
