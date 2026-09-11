from services.patient_service import *
from menus.billing_menu import process_payment, view_patient_bills

def patient_menu():
    print("\n==============================")
    print("        PATIENT LOGIN           ")
    print("================================")
    
    # Dynamic Authentication Check
    patient_record = patient_login()
    if not patient_record:
        return  # Stop execution and go back to main menu if login returns False

    while True:
        print("\n===================================")
        print("      PATIENT/USER DASHBOARD        ")
        print("=====================================")
        print("1. View Patient Profile")
        print("2. Book Appointment")
        print("3. View Patient Appointment list")
        print("4. View Patient Prescriptions")
        print("5. Update Patient Information")
        print("6. Pay The Bill")
        print("7. Download/View Bill")
        print("8. Logout")
        print("=======================================")
        choice=int(input("Enter YOUR CHOICE:"))
        match choice:
            case 1:
                search_patient_by_id(patient_record[0])
            case 2:
                book_appointment(patient_record[0])
            case 3:
                view_patient_appointments(patient_record[0])
            case 4:
                view_patient_prescriptions(patient_record[0])
            case 5:
                update_patient(patient_record[0])
            case 6:
                process_payment()
            case 7:
                view_patient_bills(patient_record[0])
            case 8:
                print("exit")
                break
            case _:
                print("invalid conditons please choose right condition")
