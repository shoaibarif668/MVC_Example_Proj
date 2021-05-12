from model import Employee

class Request():

    @staticmethod
    def viewEmployees():
        Employee.viewEmployees()
        return

    @staticmethod
    def deleteEmployee(emp):
        Employee.deleteEmployee(emp)
        print("Employee " + emp.FirstName + "Deleted from Database")
        print("Updated Data : ")
        Employee.viewEmployees()
        return

    @staticmethod
    def createNewEmployee(): 
        print("Input Information : ")
        Employee.createEmployee(
            input("EmpployeeID : "),
            input('FirstName: ') , 
            input('LastName: '), 
            input("Gender: "), 
            input( 'HiredDate: '), 
            input('Salary: ') )
        print()
        print("New Employee Created")
        return


    @staticmethod
    def updateSalary(name, salary): 
        emp = Employee.findEmployeeByName(name)
        if emp == 0:
            return "Employee Not Found"
        emp.updateSalary(salary)
        emp.viewEmployee()
        return "Salary Updated"

    @staticmethod
    def deleteEmployee(name): 
        emp = Employee.findEmployeeByName(name)
        if emp == 0:
            return "Employee Not Found"
        emp = Employee.findEmployeeByName("Mujtaba")
        Employee.deleteEmployee(emp)
        return "Employee Deleted, Database Updated"
    


Employee.viewEmployees()