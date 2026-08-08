def doctor_menu():
    while True:
        print("\n================================")
        print("       DOCTOR MODULE")
        print("================================")
        print("1. View Appointments")
        print("2. Patient History")
        print("3. Prescription")
        print("4. Discharge")
        print("5. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("View Appointments selected")

        elif choice == "2":
            print("Patient History selected")

        elif choice == "3":
            print("Prescription selected")

        elif choice == "4":
            print("Discharge selected")

        elif choice == "5":
            break

        else:
            print("Invalid choice")