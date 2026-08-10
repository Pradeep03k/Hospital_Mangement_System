from menus.billing_menu import process_payment, view_patient_bills
from services.patient_service import *


def patient_menu():
    print("\n==============================")
    print("        PATIENT LOGIN           ")
    print("================================")
    
    # Dynamic Authentication Check
    patient_record = patient_login()
    if not patient_record:
        return  # Stop execution and go back to main menu if login returns False

    while True:
        print("\n==============================")
        print("      PATIENT DASHBOARD        ")
        print("==============================")
        print("1. Add New Patient")
        print("2. View Patient Profile")
        print("3. Book Appointment")
        print("4. View Patient Appointment list")
        print("5. View Patient Prescriptions")
        print("6. Update Patient Information")
        print("7. Pay The Bill")
        print("8. Download/View Bill")
        print("9. Logout")
        print("==============================")

        choice=int(input("Enter YOUR CHOICE:"))
        match choice:
            case 1:
                add_patient()
            case 2:
                search_patient_by_id(patient_record[0])
            case 3:
                book_appointment(patient_record[0])
            case 4:
                view_patient_appointments(patient_record[0])
            case 5:
                view_patient_prescriptions(patient_record[0])
            case 6:
                update_patient(patient_record[0])
            case 7:
                process_payment()
            case 8:
                view_patient_bills(patient_record[0])
            case 9:
                print("exit")
                break
            case _:
                print("invalid conditons please choose right condition")
