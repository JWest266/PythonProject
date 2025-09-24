MyQueue = []

def Enqueue():
    r = input("Choose what you want to add")
    MyQueue.append(r)
    print("Your value has been added")

def Dequeue():
    d = input("Choose which value you would like to remove")
    MyQueue.remove(d)
    print("Your value has been removed")

while 1:
    print("1. Add a name to the list")
    print("2. Remove a name from the list")
    print("3. Show the list")

    option = input("Choose which option")

    if option == "1":
        Enqueue()

    elif option == "2":
        Dequeue()

    elif option == "3":
        print(MyQueue)