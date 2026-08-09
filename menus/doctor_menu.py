def doctor_menu():

    while True:

        print("\n================================")
        print("       DOCTOR MANAGEMENT")
        print("================================")
        print("1. Register Doctor")
        print("2. View All Doctors")
        print("3. Search Doctor")
        print("4. Update Doctor")
        print("5. Delete Doctor")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register_doctor()

        elif choice == "2":
            get_all_doctors()

        elif choice == "3":
            get_doctor_by_id()

        elif choice == "4":
            update_doctor()

        elif choice == "5":
            delete_doctor()

        elif choice == "6":
            break

        else:
            print("Invalid choice.")

