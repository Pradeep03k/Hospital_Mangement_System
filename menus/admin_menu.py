from services.admin_service import *
from services.appointment_services import *
from services.billing_services import *
from services.doctor_service import *
from services.patient_service import *
from services.receptionist_service import *

def admin_menu():
    print("\n==============================")
    print("          ADMIN LOGIN         ")
    print("==============================")
    if not admin_login():
        return  # Stop execution and go back to main menu if login returns False
    while True:
        print("1.Admin related operations")
        print("2.ALL Department Access")
        print("3.Logout")

        choice=int(input("Enter your choice:"))

        match choice:
            case 1:
                while True:
                    print("\n==============================")
                    print("      ADMIN DASHBOARD        ")
                    print("==============================")
                    print("1. View My Profile")
                    print("2. Update Admin Profile")
                    print("3. Change Admin Password")
                    print("4. Delete Admin")
                    print("5. Logout")
                    print("==============================")

                    choice = int(input("Enter your choice (1-7): "))

                    match choice:
                        case 1:
                            search_admin_by_id()
                        case 2:
                            update_admin()
                        case 3:
                            update_admin_password()
                        case 4:
                            delete_admin()
                        case 5:
                            print("Logging out...")
                            break
                        case _:
                            print("Invalid choice! Please select 1-7.")
            case 2:
                while True:
                    print("\n=====================================================")
                    print("      ADMIN ACCESS DASHBOARD  FOR ALL DEPARTMENT       ")
                    print("=======================================================")
                    print("1. DOCTOR DEPARTMENT")
                    print("2. RECEPTIONIST DEPARTMENT")
                    print("3. APPOINTMENT DEAPRTMENT")
                    print("4. BILLING DEPARTMENT")
                    print("5. PATIENT DEPARTMENT")
                    print("6. Logout")
                    print("=======================================================")

                    choice=int(input("Enter your Choce for admin which Dept u want ACCESS:"))
                    match choice:
                        case 1:
                            while True:
                                    print("\n==============================")
                                    print("      DOCTOR DASHBOARD        ")
                                    print("==============================")
                                    print("1. Add New Doctor")
                                    print("2. Search Doctor")
                                    print("3. View All Doctors")
                                    print("4. view Doctor Appointment")
                                    print("5. Update Doctor Profile")
                                    print("6. Delete Doctor")
                                    print("7. LOGOUT...!")
                                    print("==============================")
                            
                                    choice=int(input("Enter the choice:"))
                                    match choice:
                                        case 1:
                                            add_doctor()
                                        case 2:
                                            search_doctor_by_id()
                                        case 3:
                                            view_all_doctors()
                                        case 4:
                                            doctor_id = int(input("Enter Doctor ID: "))
                                            view_doctor_appointments(doctor_id)
                                        case 5:
                                            doctor_id = int(input("Enter Doctor ID: "))
                                            update_doctor_profile(doctor_id)
                                        case 6:
                                            delete_doctor()
                                        case 7:
                                            print("Login out....")
                                            break
                                        case _ :
                                            print("invalid choice please choose right options...")
                        case 2:
                            while True:
                                    print("\n==============================")
                                    print("    RECEPTIONIST DASHBOARD    ")
                                    print("==============================")
                                    print("1. Add New Receptionist")
                                    print("2. View All Receptionist")
                                    print("3. Search Receptionist")
                                    print("4. Update Receptionist Profile")
                                    print("5. Change Password")
                                    print("6. Delete Receptionist")
                                    print("7. Logout")
                                    print("==============================")
                            
                                    choice = int(input("Enter your choice (1-7): "))
                            
                                    match choice:
                                        case 1:
                                            add_receptionist()
                                        case 2:
                                            view_receptionist()
                                        case 3:
                                            search_receptionist_by_id()
                                        case 4:
                                            update_receptionist()
                                        case 5:
                                            update_receptionist_password()
                                        case 6:
                                            delete_receptionist()
                                        case 7:
                                            print("Logging out from Receptionist Module...")
                                            break
                                        case _:
                                            print("Invalid choice! Please select 1-7.")
                        case 3:
                            while True:
                                print("\n==============================")
                                print("      APPOINTMENT DASHBOARD     ")
                                print("================================")
                                print("1. View All Appointment")
                                print("2. Update Appointment")
                                print("3. Cancel Appointment")
                                print("4. Exit")
                                print("\n=============================")

                                choice=int(input("Enter your Choice:"))
                                match choice:
                                    case 1: 
                                        view_all_appointments()
                                    case 2:
                                        update_appointment_status()
                                    case 3:
                                        delete_appointment()
                                    case 4:
                                        print("Exit")
                                        break
                                    case _ :
                                        print("invalid choice please make choice right")
                        case 4:
                            while True:
                                print("\n==============================")
                                print("      BILLING DASHBOARD        ")
                                print("================================")
                                print("1.View all Bill")
                                print("2.Update the Bills")
                                print("3.Delete Bill")
                                print("4.Exit")

                                choice=int(input("Enter your choice:"))
                                match choice:
                                    case 1:
                                        view_all_bills()
                                    case 2:
                                        update_bill()
                                    case 3:
                                        delete_patient_bill_admin()
                                    case 4:
                                        print("Exit")
                                        break
                                    case _ :
                                        print("invalid choice please enter valid choice")
                        case 5:
                            while True:
                                    print("\n==============================")
                                    print("      PATIENT DASHBOARD        ")
                                    print("==============================")
                                    print("1. View All Patient")
                                    print("2. Update Patient Information")
                                    print("3. Delete Patient Information")
                                    print("4. Exit")
                                    print("==============================")
                            
                                    choice=int(input("Enter YOUR CHOICE:"))
                                    match choice:
                                        case 1:
                                            view_all_patients()
                                        case 2:
                                            patient_id = int(input("Enter Patient ID: "))
                                            update_patient(patient_id)
                                        case 3:
                                            delete_patient()
                                        case 4:
                                            print("Exit")
                                            break
                                        case _ :
                                            print("invalid choice please choose right option")
                        case 6:
                            print("Logout")
                            break
            case 3: 
                print("Log out")
                break
            case _ :
                print("Invalid conditons please choose right options")

                                                                             
                                               
