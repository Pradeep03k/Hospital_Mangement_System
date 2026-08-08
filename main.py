from menus.doctor_menu import doctor_menu
from menus.patient_menu import patient_menu


def main():
    while True:
        print("\n======================================")
        print("       HOSPITAL MANAGEMENT SYSTEM")
        print("======================================")

        print("1. Doctor Module")
        print("2. Patient Module")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            doctor_menu()

        elif choice == "2":
            patient_menu()

        elif choice == "3":
            print("Thank you for using Hospital Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()