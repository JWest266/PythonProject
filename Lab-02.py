myEmployees = {}

while True:
    print("1. Add an Employee")
    print("2. Delete an Employee")
    print("3. modify an Employee")
    print("4. Display all the Employee")
    print("5. Exit the program")

    option = input()

    if option == "1":
        empid = input("Enter Employee ID, ")
        nname = input("Employee name, ")
        ppay =  int(input("Basic pay, "))
        alllowence =  int(input("Allowance, "))
        ddeduction = int(input("Deduction, "))
        taxx = int(input("Taxes, "))

        Netpay = (ppay+alllowence)

        GrossPay = Netpay - (ddeduction + taxx)


        myEmployees[empid] = {
            "Employee ID": empid,
            "Employee Name": nname,
            "Allowance": alllowence,
            "Deductions": ddeduction,
            "Basic Pay": ppay,
            "NetPay": Netpay,
            "GrossPay": GrossPay
}
    elif option == "2":
        empid = input("Enter ID of Employee you would like to delete, ")
        if empid in myEmployees:
            del myEmployees[empid]

    elif option == "3":
        empid = input("Enter ID of Employee you would like to modify: ")

        if empid in myEmployees:
            nname = input("Enter new name,  ")
            ppay = int(input("Basic pay, "))
            alllowence = int(input("Allowance,  "))
            ddeduction = int(input("Deduction,  "))
            taxx = int(input("Taxes,  "))

            netpay = ppay + alllowence
            GrossPay = netpay - (ddeduction + taxx)

            myEmployees[empid] = {
                "Employee ID": empid,
                "Employee Name": nname,
                "Allowance": alllowence,
                "Deductions": ddeduction,
                "Basic Pay": ppay,
                "NetPay": netpay,
                "GrossPay": GrossPay
            }

    elif option == "4":
        print(myEmployees)
        print("------------------------")

    elif option == "5":
        print("Exiting program")
        break







