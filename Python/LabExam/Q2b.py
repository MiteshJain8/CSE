# Write a python program to create a list with all the subject names of the 4th semester and perform the following operations. 
# Display 2nd and 5th element of the list. 
# Display the list using for loop. 
# Display first 4 elements of the list using the range of indexes. 
# Display last 4 elements of the list using the range of negative indexes. 
# Display if "Python Programming Lab" is available in the List or not. 
# Demonstrate the working of append () and insert () function. 
# Demonstrate the working of remove() and pop() function

subjects = ["Maths", "MC&IoT", "DAA", "DCN", "FAFL", "DAA Lab", "DCN lab", "Python Programming Lab", "Data Analysis with R"]

print("All subjects:")
for subject in subjects:
    print(subject)

print("\n2nd and 5th subjects:")
print(subjects[1])
print(subjects[4])

print("\nFirst 4 subjects:")
print(subjects[:4])

print("\nLast 4 subjects:")
print(subjects[-4:])

if "Python Programming Lab" in subjects:
    print("\nPython Programming Lab is available in the list.")
else:
    print("\nPython Programming Lab is not available in the list.")

subjects.append("New Subject")
print("\nAfter appending a new subject:")
print(subjects)

subjects.insert(2, "Inserted Subject")
print("\nAfter inserting a subject at the 3rd position:")
print(subjects)

subjects.remove("New Subject")
print("\nAfter removing the new subject:")
print(subjects)

subjects.pop(2)
print("\nAfter popping the subject at the 3rd position: ")
print(subjects)