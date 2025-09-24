MyStack = []

def AddStack():
    a = input("add a value to the stack")
    MyStack.append(a)

def RemoveStack():
    print("Would you like to remove from the stack")
    print("1. Yes")
    print("2. No")
    option = input("Make your choice")

    if option == "1":
        MyStack.pop()
    elif option == "2":

