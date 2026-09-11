from services.appointment_services import *

def appointment_menu(): 
    while True:
        print("\n==============================")
        print("      APPOINTMENT DASHBOARD     ")
        print("================================")
        print("1. Book Appointment")
        print("2. View All Appointment")
        print("3. Update Appointment")
        print("4. Cancel Appointment")
        print("5. Exit")
        print("\n=============================")
    
        choice=int(input("Enter your Choice:"))
        match choice:
            case 1:
                patient_id = int(input("Enter Patient ID: "))
                book_appointment(patient_id)
            case 2: 
                view_all_appointments()
            case 3:
                update_appointment_status()
            case 4:
                delete_appointment()
            case 5:
                print("Exit")
                break
            case _ :
                print("invalid choice please make choice right")