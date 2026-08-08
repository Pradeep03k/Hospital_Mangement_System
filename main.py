from menus.doctor_menu import doctor_menu
from menus.patient_menu import patient_menu


def main():

    while True:

        print("\n===================================")
        print("     HOSPITAL MANAGEMENT SYSTEM")
        print("===================================")

        print("1. Doctor Module")
        print("2. Patient Module")
        print("3. Exit")

        choice = input("Enter Your Choice : ")

        if choice == "1":

            doctor_menu()

        elif choice == "2":

            patient_menu()

        elif choice == "3":

            print("\nThank You...")
            break

        else:

            print("Invalid Choice")


if __name__ == "__main__":
    main()