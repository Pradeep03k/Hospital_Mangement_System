from services.doctor_service import *

def doctor_menu():
    print("\n==============================")
    print("        DOCTOR LOGIN           ")
    print("================================")
    
    doctor_record = doctor_login()
    if not doctor_record:
        return 

    while True:
        print("\n==============================")
        print("      DOCTOR DASHBOARD        ")
        print("==============================")
        print("1. View Doctor Profile")
        print("2. view Appointments")
        print("3. Add Patient Prescription")
        print("4. Update Doctor Profile")
        print("5. LOGOUT...!")
        print("==============================")

        choice=int(input("Enter the choice:"))
        match choice:
            case 1:
                search_doctor_by_id()
            case 2:
                view_doctor_appointments(doctor_record[0])
            case 3:
                add_prescription(doctor_record[0])
            case 4:
                update_doctor_profile(doctor_record[0])
            case 5:
                print("Login out....")
                break
            case _ :
                print("invalid choice please choose right options...")
            