# Develop a python program to create a class called as Employee with attributes like EmpID, EmpName, EmpDesignation, Experience and Age. Write the methods for addEmployee(), displayDetails() and calculateSalary(float basic). The salary of an employee should be calculated based on the following criteria: 
# If the employee is below 30 years with 5+ experience then the final salary 1.5 * basic. 
# If the employee is below 40 years with 5+ experience then the final salary 1.75 * basic. 
# If the employee is below 40 years with 10+ experience then the final salary 2 * basic. 
# If the employee is below 50 years with 20+ experience then the final salary 2.25 * basic. 
# If the employee is below 50 years with 25+ experience then the final salary 2.5 * basic. 
# If the employee is below 58 years with 30+ experience then the final salary 3 * basic.

class Employee:
    Emp_list = []
    def __init__(self, emp_id, emp_name, emp_designation, experience, age):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_designation = emp_designation
        self.experience = experience
        self.age = age

    def add_employee(self):
        Employee.Emp_list.append(self)

    def calculate_salary(self, basic):
        if self.age < 30 and self.experience >= 5:
            salary = 1.5 * basic
        elif self.age < 40 and self.experience >= 5:
            salary = 1.75 * basic
        elif self.age < 40 and self.experience >= 10:
            salary = 2 * basic
        elif self.age < 50 and self.experience >= 20:
            salary = 2.25 * basic
        elif self.age < 50 and self.experience >= 25:
            salary = 2.5 * basic
        elif self.age < 58 and self.experience >= 30:
            salary = 3 * basic
        else:
            salary = basic
        return salary

    def display_details(self):
        print("Employee ID:", self.emp_id)
        print("Employee Name:", self.emp_name)
        print("Employee Designation:", self.emp_designation)
        print("Experience:", self.experience)
        print("Age:", self.age)
        print("Salary:", self.calculate_salary(50000))
        print()

emp1 = Employee(1, "Anu", "Software Engineer", 10, 30)
emp2 = Employee(2, "Anuj", "Data Analyst", 15, 35)
emp1.add_employee()
emp2.add_employee()
for emp in Employee.Emp_list:
    emp.display_details()