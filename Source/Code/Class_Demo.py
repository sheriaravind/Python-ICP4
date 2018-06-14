class Employee(object):
    employee_count=0
    totalsal=0
    avgsal=0

    def __init__(self,name,family,sal,dept): # init method in the class to instantiate the class member variables
        self.name = name
        self.family = family
        self.salary = sal
        self.department = dept
        Employee.employee_count += 1
        Employee.totalsal += sal

    def avgsalary(self):
        avgsal=Employee.totalsal/Employee.employee_count
        print("Average Salary of Employees:",avgsal)

    def calcemployees(self):
        print("Total Employees are:",Employee.employee_count)

    def displayDetails(self):
        print("Name:",self.name,"Family:",self.family,"Salary:",self.salary,"Department:",self.department)


class FullTimeEmployee(Employee): # Created a class which inherits the members of class Employee
    def _init_(self,n,f,s,d):
        Employee._init_(self,n,f,s,d)



e1 = Employee("John","SE",3000,"Testing") # Created an object and instantiated the members of the class
e2 = Employee("Tom","AM",4000,"Artificial Inteligence")
e3 = Employee("Jonathan","SSE",7000,"HR" )
fe1=FullTimeEmployee("Robert","SSE",5000,"Development") # Created an object of the sub class FullTimeEmployee
fe2=FullTimeEmployee("Ross","SM",6000,"Management")

e1.displayDetails()
e1.displayDetails()
fe1.displayDetails()
fe2.displayDetails() # Calling the method of the super class using the sub class object

fe2.avgsalary()
fe2.calcemployees()