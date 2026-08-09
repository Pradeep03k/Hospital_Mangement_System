from services.billing_services import *
def billing_menu():
    while True:
        print("\n==============================")
        print("      BILLING DASHBOARD        ")
        print("================================")
        print("1.Add Bill")
        print("2.View all Bill")
        print("3.Payment Process")
        print("4.Update Bill")
        print("5.Delete Bill")
        print("6.Exit")
    
        choice=int(input("Enter your choice:"))
        match choice:
            case 1:
                create_bill()
            case 2:
                view_all_bills()
            case 3:
                process_payment()
            case 4:
                update_bill()
            case 5:
                delete_patient_bill_admin()
            case 6:
                print("exit")
            case _:
                print("invalid choice please choose right option")