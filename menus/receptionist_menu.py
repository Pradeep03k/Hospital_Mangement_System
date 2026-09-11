from services.receptionist_service import *
from services.appointment_services import *
from services.billing_services import *

def receptionist_menu():
    print("\n==============================")
    print("      RECEPTIONIST LOGIN      ")
    print("==============================")

    # Dynamic Authentication Check
    if not receptionist_login():
        return  # Stops execution and goes back to main menu if login returns False

    while True:
        print("\n==============================")
        print("    RECEPTIONIST DASHBOARD    ")
        print("==============================")
        print("1. View All Receptionits")
        print("2. View Receptionits Profile")
        print("3. Update Receptionist Profile")
        print("4. Change Password")
        print("5. View all appointments")
        print("6. Genrate Patient Bill")
        print("7. Logout")
        print("==============================")

        choice = int(input("Enter your choice (1-8): "))

        match choice:
            case 1:
                view_receptionist()
            case 2:
                search_receptionist_by_id()
            case 3:
                update_receptionist()
            case 4:
                update_receptionist_password()
            case 5:
                view_all_appointments()
            case 6:
                create_bill()
            case 7:
                print("Logging out from Receptionist Module...")
                break
            case _:
                print("Invalid choice! Please select 1-8.")
