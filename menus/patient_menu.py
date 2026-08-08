def patient_menu():
    while True:
        print("\n================================")
        print("       PATIENT MODULE")
        print("================================")
        print("1. Search Doctor")
        print("2. Book Appointment")
        print("3. View Prescription")
        print("4. Payment")
        print("5. Download Bill")
        print("6. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Search Doctor selected")

        elif choice == "2":
            print("Book Appointment selected")

        elif choice == "3":
            print("View Prescription selected")

        elif choice == "4":
            print("Payment selected")

        elif choice == "5":
            print("Download Bill selected")

        elif choice == "6":
            break

        else:
            print("Invalid choice")