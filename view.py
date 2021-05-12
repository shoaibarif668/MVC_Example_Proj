from controller import Request

authentication = False
while not authentication:
    print("Authenticate yourself ")
    passw = str(input("Input Password : "))
    if passw == '12345':
        authentication = True
    else:
        print("Wrong Password, Try Again.")

exit = False
while not exit:
    print()
    print("\nPlease Select Number")
    print("\n0 to exit")
    print("\n1 to view Employees Data")
    print("\n2 to Add Employee")
    print("\n3 to Update Employee Salary")        
    print("\n4 to delete an Employee")
    print()

    selection = str(input())
    if selection == '0':
        print("Exiting Application ....  \n ")
        exit = True

    elif selection == '1':
        Request.viewEmployees()


    elif selection == '2':
        print("Add a new Employee : ")
        Request.createNewEmployee()
    
    elif selection == '3':
        print("Input Employee First name : ")
        name = str(input())
        print("Input Salary : ")
        salary = str(input())
        print(Request.updateSalary(name, salary))
    
    elif selection == '4':
        print("Input Employee First name to delete: ")
        name = str(input())
        print( Request.deleteEmployee(name) )
    
    else:
        print("Wrong Selection")