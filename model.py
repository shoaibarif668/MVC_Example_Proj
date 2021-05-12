from database import employees


class Employee:
    def __init__(self, number):
        cursor = employees[number]
        self.number     = number
        self.EmployeelD = cursor['EmployeelD']
        self.FirstName  = cursor['FirstName']
        self.LastName   = cursor['LastName']
        self.Gender     = cursor['Gender']
        self.HiredDate  = cursor['HiredDate']
        self.Salary     = cursor['Salary']

    @staticmethod
    def createEmployee(EmployeelD , FirstName , LastName, Gender, HiredDate, Salary):
        number = len(employees)
        dict_ = {
        'EmployeelD' : EmployeelD,
        'FirstName'  : FirstName,
        'LastName'   : LastName,
        'Gender'     : Gender,
        'HiredDate'  : HiredDate,
        'Salary'     : Salary  
        }

        employees.append(dict_)
        return

    def viewEmployee(self):
        print()
        print("ID :", self.EmployeelD)
        print('FirstName :', self.FirstName )
        print('LastName :', self.LastName  )
        print('Gender :', self.Gender    )
        print('HiredDate : ', self.HiredDate )
        print('Salary : ', self.Salary    )
        print()
        return

    def updateSalary(self, newSalary):
        self.Salary = newSalary
        employees[self.number]["Salary"] =  newSalary
        return

    def updateHiredDate(self, newHiredDate):
        self.HiredDate = newHiredDate
        employees[self.number]["HiredDate"] =  newHiredDate
        return

    def updateEmployeelD(self, newemployeelD):
        self.EmployeelD = newemployeelD
        employees[self.number]["EmployeelD"] =  newemployeelD
        return

    @staticmethod
    def deleteEmployee(emp):
        dic = {}
        print(emp.__dict__)
        for i in emp.__dict__:
            if i!='number':
                dic[i] = emp.__dict__[i]
        employees.remove(dic)
        print()
        print("Employee deleted")
        return

    @staticmethod
    def viewEmployees():
        print()
        for i in employees:
            for j in i:
                print(j,  ' : ',i[j])
            print()
        return

    
    @staticmethod 
    def findEmployeeByName(name):
        count = 0
        for i in employees:
            if i['FirstName'] == name:
                emp = Employee(count)
                return (emp)
            count+=1
        return 0

