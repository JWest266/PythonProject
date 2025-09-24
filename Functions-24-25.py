def area_rectangle():
    l = int(input("Enter Length"))
    b = int(input("Enter Breadth"))
    print(l*b)

def volume_cube ():
    l = int(input("Enter length"))
    b = int(input("Enter Breadth"))
    h = int(input("Enter Heigth"))
    print(l*b*h)
def area_circle():
    r = int(input("Enter the radius"))
    print(3.14*r*r)

def volume_circle():
    r = int(input("Enter the radius"))
    print(2*3.14*r)

def volume_sphere():
    r = int(input("Enter Radius"))
    print((4/3)*3.14*r*r*r)

#Main Code
while 1:
    print("1. Area of Rectangle")
    print("2. Volume of a cube")
    print("3. Area of a circle")
    print("4. Volume of a circle")
    print("5. Volume of a sphere")
    print("6. Quit Application")

    option = input("Enter your choice:", )

    if option == "1":
        area_rectangle()

    elif option == "2":
        volume_cube()

    elif option == "3":
        area_circle()

    elif option == "4":
        volume_circle()

    elif option == "5":
        volume_sphere()

    elif option == "6":
        answer = input("Are you sure you would like to Quit? ")
        if answer == "yes":
            answer2 = input("please don't quit i spent so much time on this: Type I don't care/ ok")
            if answer2 == "I don't care":
                break
            elif answer2 == "ok":
                print("good")
        elif answer == "no":
            print("Good")