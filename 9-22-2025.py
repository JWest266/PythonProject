Projects = {}
mang = []
tec = []
team = []
while True:
    print("1. Project Initiation")
    print("2. Project Closure")
    print("3. Project Progress Update")
    print("4. Print a specific Project")
    print("5. Print All Projects")
    print("6. Quit Application")
    choice = input("Please Enter an option: ")

    if choice == "1":
        PID = input("Enter project ID: ")
        Title = input("Enter Project Title: ")
        m = int(input("How many managers do you want to enter: "))
        for i in range (0, m):
            mang.append(input("Enter Manager's name: "))

        SD = input("Enter Start date: ")
        ED = input ("Enter End Date: ")
        Spon = input("Enter a sponsor: ")
        budget = input("Enter a Budget: ")

        te = int(input("How many Technologies are being used: "))
        for i in range(0, te):
            tec.append(input("Enter Technologies: "))

        Tea = int(input("How many team members are going to be added: "))
        for i in range(0, Tea):
            team.append(input("Enter Team member's names"))

        Projects.update({ PID: {
            "Project_title": Title,
            "Managers": mang,
            "Start_Date": SD,
            "End_Date": ED,
            "Sponsor": Spon,
            "Budget": budget,
            "Technologies": tec,
            "Team Members": team
        }})

    elif choice == "2":
        P = int(input("Enter Project ID of finished Project: "))
        if P in Projects:
            del Projects[PID]

    elif choice == "5":
        print(Projects)