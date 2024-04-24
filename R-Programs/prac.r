# write a r script that maintains student details (roll number, name ,  marks od students) find total and average marks. Check wether a student has passed or failed in every subject. Display details of the student

student<- c("Mamata", 69, 100, 20, 22)
print(student)
t=as.numeric(student[3])+as.numeric(student[4])+as.numeric(student[5])
typeof(t)
