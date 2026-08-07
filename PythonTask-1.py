"""Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student's name is not found, display an appropriate message.
"""


#Dictonary of student_marks with student name as key and marks as values
student_marks = {
    "Peter": 85,
    "Jean": 90,
    "Mary": 78,
    "Ned": 92,
    "Frank": 88
}
# Ask the user for input
name = input("Enter the student's name: ")

if name in student_marks:
        print(f"{name}'s marks: {student_marks[name]}")
else:

  print("Student not found.")
