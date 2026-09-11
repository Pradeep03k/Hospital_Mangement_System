from Database.db import conn, cursor
from models.patient import Patient


def patient_login():
    email = input("Enter patient email: ")
    password = input("Enter patient password: ")

    query = "SELECT patient_id, name FROM patients WHERE email = %s AND password = %s"
    cursor.execute(query, (email, password))
    patient_record = cursor.fetchone()

    if patient_record is not None:
        print(f"\nLogin Successful! Welcome, {patient_record[1]}.")
        return patient_record  # Returns tuple: (patient_id, name)
    else:
        print("\nInvalid Email or Password! Access Denied.")
        return None


def add_patient():
    name = input("Enter patient name: ")
    email = input("Enter patient email: ")
    password = input("Enter patient password: ")
    phone = input("Enter phone number: ")
    age = int(input("Enter age: "))
    gender = input("Enter gender (Male/Female/Other): ")
    if gender not in ['Male', 'Female', 'Other']:
        gender = 'Other'
    address = input("Enter residential address: ")

    p = Patient(None,name, email, password, phone, age, gender, address)

    cursor.execute("SELECT * FROM patients WHERE email = %s", (p.email,))
    if cursor.fetchone() is not None:
        print("Patient with this email already exists!")
        return

    query = "INSERT INTO patients (name, email, password, phone, age, gender, address) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (p.name, p.email, p.password, p.phone, p.age, p.gender, p.address))
    conn.commit()
    print("Patient registered successfully!")


def view_all_patients():
    cursor.execute("SELECT patient_id, name, email, phone, age, gender FROM patients")
    rows = cursor.fetchall()
    if not rows:
        print("No patients found.")
        return
    for row in rows:
        print(f"ID: {row[0]} | Name: {row[1]} | Email: {row[2]} | Phone: {row[3]} | Age: {row[4]} | Gender: {row[5]}")


def search_patient_by_id(patient_id=None):
    if patient_id is None:
        patient_id = int(input("Enter Patient ID: "))

    query = "SELECT patient_id, name, email, phone, age, gender, address, created_at FROM patients WHERE patient_id = %s"
    cursor.execute(query, (patient_id,))
    row = cursor.fetchone()

    if row is None:
        print("Patient record not found.")
        return

    print("\n--- Patient Profile Details ---")
    print(f"ID         : {row[0]}")
    print(f"Name       : {row[1]}")
    print(f"Email      : {row[2]}")
    print(f"Phone      : {row[3]}")
    print(f"Age        : {row[4]}")
    print(f"Gender     : {row[5]}")
    print(f"Address    : {row[6]}")
    print(f"Registered : {row[7]}")
    print("-------------------------------\n")


def book_appointment(patient_id):
    # Display available doctors
    cursor.execute("SELECT doctor_id, name, specialization, consultation_fee FROM doctors")
    doctors = cursor.fetchall()

    if not doctors:
        print("No doctors available for booking at the moment.")
        return

    print("\n--- Available Doctors ---")
    for doc in doctors:
        print(f"ID: {doc[0]} | Dr. {doc[1]} ({doc[2]}) | Fee: ${doc[3]}")

    doc_id = int(input("\nEnter Doctor ID to book: "))
    appt_date = input("Enter appointment date (YYYY-MM-DD): ")
    appt_time = input("Enter appointment time (HH:MM:SS): ")
    reason = input("Reason for visit: ")

    query = "INSERT INTO appointments (patient_id, doctor_id, appointment_date, appointment_time, reason_for_visit) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (patient_id, doc_id, appt_date, appt_time, reason))
    conn.commit()
    print("Appointment request submitted successfully! Current Status: Pending.")


def view_patient_appointments(patient_id):
    query = """
    SELECT a.appointment_id, d.name, a.appointment_date, a.appointment_time, a.status, a.reason_for_visit
    FROM appointments a
    JOIN doctors d ON a.doctor_id = d.doctor_id
    WHERE a.patient_id = %s
    ORDER BY a.appointment_date DESC
    """
    cursor.execute(query, (patient_id,))
    rows = cursor.fetchall()

    if not rows:
        print("No appointment history found.")
        return

    print("\n--- My Appointments ---")
    for r in rows:
        print(f"ID: {r[0]} | Doctor: Dr. {r[1]} | Date: {r[2]} | Time: {r[3]} | Status: {r[4]} | Reason: {r[5]}")


def view_patient_prescriptions(patient_id):
    query = """
    SELECT pr.prescription_id, d.name, pr.medicines_prescribed, pr.doctor_notes, pr.issued_date
    FROM prescriptions pr
    JOIN doctors d ON pr.doctor_id = d.doctor_id
    WHERE pr.patient_id = %s
    """
    cursor.execute(query, (patient_id,))
    rows = cursor.fetchall()

    if not rows:
        print("No prescriptions issued yet.")
        return

    print("\n--- My Prescriptions ---")
    for r in rows:
        print(f"Prescription ID: {r[0]} | Issued By: Dr. {r[1]}\nMedicines: {r[2]}\nNotes: {r[3]}\nDate: {r[4]}\n" + "-"*40)


def delete_patient():
    userip = int(input("Enter Patient ID to delete: "))

    cursor.execute("SELECT * FROM patients WHERE patient_id = %s", (userip,))
    if cursor.fetchone() is None:
        print("Patient ID does not exist.")
        return

    cursor.execute("DELETE FROM patients WHERE patient_id = %s", (userip,))
    conn.commit()
    print("Patient record deleted successfully!")

# Update Patient Profile
def update_patient(patient_id=None):
    if patient_id is None:
        patient_id = int(input("Enter Patient ID to update: "))

    cursor.execute("SELECT * FROM patients WHERE patient_id = %s", (patient_id,))
    existing_patient = cursor.fetchone()

    if existing_patient is None:
        print("Patient ID not found!")
        return

    print("\n--- Update Patient Information ---")
    name = input("Enter updated name: ")
    email = input("Enter updated email: ")
    phone = input("Enter updated phone number: ")
    age = int(input("Enter updated age: "))
    gender = input("Enter updated gender (Male/Female/Other): ")
    if gender not in ['Male', 'Female', 'Other']:
        gender = 'Other'
    address = input("Enter updated residential address: ")

    query = """
    UPDATE patients 
    SET name = %s, email = %s, phone = %s, age = %s, gender = %s, address = %s 
    WHERE patient_id = %s
    """
    values = (name, email, phone, age, gender, address, patient_id)
    cursor.execute(query, values)
    conn.commit()
    print("\nPatient profile updated successfully!")