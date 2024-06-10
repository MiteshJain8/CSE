# Develop a python program to create a text file and ask the user to enter their details like USN, Name, Semester, Subjects and CGPA in different lines. Display the details of the file

usn = input("Enter USN: ")
name = input("Enter Name: ")
sem = input("Enter Semester: ")
subs = input("Enter Subjects: ")
cgpa = input("Enter CGPA: ")

filename = "w6p1.txt"

with open(filename, "w") as file:
    file.write(f"USN: {usn}\n")
    file.write(f"Name: {name}\n")
    file.write(f"Semester: {sem}\n")
    file.write(f"Subjects: {subs}\n")
    file.write(f"CGPA: {cgpa}")

print("\nDetails:")
with open(filename, "r") as file:
    print(file.read())