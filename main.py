

from menus.admin_menu import admin_menu,add_admin
from menus.receptionist_menu import receptionist_menu,add_receptionist
from menus.doctor_menu import *
from menus.appointment_menu import *
from menus.patient_menu import *

def main():
    
    while True:
        print("\n==========================================")
        print("       HOSPITAL MANAGEMENT SYSTEM        ")
        print("==========================================")
        print("1. Admin Module")
        print("2. Doctor Module")
        print("3. Patient Module")
        print("4. Receptionist Module")
        print("5. Exit Application")
        print("==========================================")
        
        choice = int(input("Enter your choice (1-5): "))

        match choice:
            case 1:
                choice=int(input("1.Register Admin\n2.Admin Login\n3.Exit\nEnter Admin choice:"))
                match choice:
                    case 1:
                          add_admin()
                    case 2:
                          admin_menu()
                    case 3:   
                          print("Exit")
                          break
                    case _ :
                          print("choose valid option")        
            case 2:
                choice=int(input("1.Register Doctor\n2.Doctor Login\n3.Exit\nEnter Doctor choice:"))
                match choice:
                    case 1:
                          add_doctor()
                    case 2:
                          doctor_menu()
                    case 3:   
                          print("Exit")
                          break
                    case _ :
                          print("choose valid option") 
            case 3:
                    choice=int(input("1.Register Patient\n2.Patient Login\n3.Exit\nEnter Pateint choice:"))
                    match choice:
                        case 1:
                              add_patient()
                        case 2:
                              patient_menu()
                        case 3:   
                              print("Exit")
                              break
                        case _ :
                              print("choose valid option") 
            case 4:
                   choice=int(input("1.Register Receptionist\n2.Receptionist Login\n3.Exit\nEnter Receptionist choice:"))
                   match choice:
                       case 1:
                             add_receptionist()
                       case 2:
                             receptionist_menu()
                       case 3:   
                             print("Exit")
                             break
                       case _ :
                             print("choose valid option") 
            case 5:
                print("\nThank you for using Hospital Management System. Goodbye!")
                break
            case _:
                print("\nInvalid choice! Please select a valid option between 1 and 5.")

if __name__ == "__main__":
    main()