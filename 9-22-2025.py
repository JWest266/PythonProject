Projects = {}

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

        mang = []
        m = int(input("How many managers do you want to enter: "))
        for i in range(0, m):
            mang.append(input("Enter Manager's name: "))

        SD = input("Enter Start date: ")
        ED = input("Enter End Date: ")
        Spon = input("Enter a sponsor: ")
        budget = input("Enter a Budget: ")

        tec = []
        te = int(input("How many Technologies are being used: "))
        for i in range(0, te):
            tec.append(input("Enter Technologies: "))

        team = []
        Tea = int(input("How many team members are going to be added: "))
        for i in range(0, Tea):
            team.append(input("Enter Team member's names: "))

        Projects.update({PID: {
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
        PID = (input("Enter Project ID of finished Project: "))
        if PID in Projects:
            del Projects[PID]

    elif choice == "3":
        PID = input("Enter Project ID to update: ")
        if PID not in Projects:
            print(f"Project {PID} not found.")
        else:
            project = Projects[PID]

            print("Select what to update:")
            print("1. Title")
            print("2. Managers")
            print("3. Start Date")
            print("4. End Date")
            print("5. Sponsor")
            print("6. Budget")
            print("7. Technologies")
            print("8. Team Members")
            print("9. Cancel")

            field_choice = input("Enter option number to update: ")

            if field_choice == "1":
                new_title = input("Enter new Project Title: ")
                project["Project_title"] = new_title
                print("Title updated.")

            elif field_choice == "2":
                print("Current Managers:", project["Managers"])
                update_type = input("Type 'replace' to overwrite or 'add' to add new managers: ").lower()
                if update_type == "replace":
                    new_managers = []
                    m = int(input("How many managers to enter: "))
                    for _ in range(m):
                        new_managers.append(input("Enter Manager's name: "))
                    project["Managers"] = new_managers
                    print("Managers replaced.")
                elif update_type == "add":
                    m = int(input("How many managers to add: "))
                    for _ in range(m):
                        manager = input("Enter Manager's name: ")
                        project["Managers"].append(manager)
                    print("Managers added.")
                else:
                    print("Invalid option. No changes made.")

            elif field_choice == "3":
                new_start = input("Enter new Start Date: ")
                project["Start_Date"] = new_start
                print("Start Date updated.")

            elif field_choice == "4":
                new_end = input("Enter new End Date: ")
                project["End_Date"] = new_end
                print("End Date updated.")

            elif field_choice == "5":
                new_sponsor = input("Enter new Sponsor: ")
                project["Sponsor"] = new_sponsor
                print("Sponsor updated.")

            elif field_choice == "6":
                new_budget = input("Enter new Budget: ")
                project["Budget"] = new_budget
                print("Budget updated.")

            elif field_choice == "7":
                print("Current Technologies:", project["Technologies"])
                update_type = input("Type 'replace' to overwrite or 'add' to add new technologies: ").lower()
                if update_type == "replace":
                    new_tec = []
                    t = int(input("How many technologies to enter: "))
                    for _ in range(t):
                        new_tec.append(input("Enter Technology: "))
                    project["Technologies"] = new_tec
                    print("Technologies replaced.")
                elif update_type == "add":
                    t = int(input("How many technologies to add: "))
                    for _ in range(t):
                        tech = input("Enter Technology: ")
                        project["Technologies"].append(tech)
                    print("Technologies added.")
                else:
                    print("Invalid option. No changes made.")

            elif field_choice == "8":
                print("Current Team Members:", project["Team Members"])
                update_type = input("Type 'replace' to overwrite or 'add' to add new team members: ").lower()
                if update_type == "replace":
                    new_team = []
                    tm = int(input("How many team members to enter: "))
                    for _ in range(tm):
                        new_team.append(input("Enter Team member's name: "))
                    project["Team Members"] = new_team
                    print("Team members replaced.")
                elif update_type == "add":
                    tm = int(input("How many team members to add: "))
                    for _ in range(tm):
                        member = input("Enter Team member's name: ")
                        project["Team Members"].append(member)
                    print("Team members added.")
                else:
                    print("Invalid option. No changes made.")

            elif field_choice == "9":
                print("Update cancelled.")

            else:
                print("Invalid option.")

    elif choice == "4":
        PiD = input("Which project do you want to print: ")
        if PiD in Projects:
            print(Projects[PiD])
        if PiD not in Projects:
            print("")


    elif choice == "5":
        print(Projects)