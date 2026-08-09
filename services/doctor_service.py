from Database.db import conn, cursor
from models.doctor import Doctor


def doctor_login():
    email = input("Enter doctor email: ")
    password = input("Enter doctor password: ")

    query = "SELECT doctor_id, name, specialization FROM doctors WHERE email = %s AND password = %s"
    cursor.execute(query, (email, password))
    doc_record = cursor.fetchone()

    if doc_record is not None:
        print(f"\nLogin Successful! Welcome Dr. {doc_record[1]} ({doc_record[2]}).")
        return doc_record  # Returns tuple: (doctor_id, name, specialization)
    else:
        print("\nInvalid Email or Password! Access Denied.")
        return None


def add_doctor():
    name = input("Enter doctor name: ")
    specialization = input("Enter specialization: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    phone = input("Enter phone: ")
    fee_input = input("Enter consultation fee (Default 500.00): ")
    fee = float(fee_input) if fee_input else 500.00

    d = Doctor(name, specialization, email, password, phone, fee)

    cursor.execute("SELECT * FROM doctors WHERE email = %s", (d.email,))
    if cursor.fetchone() is not None:
        print("Doctor email already exists!")
        return

    query = "INSERT INTO doctors (name, specialization, email, password, phone, consultation_fee) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (d.name, d.specialization, d.email, d.password, d.phone, d.consultation_fee))
    conn.commit()
    print("Doctor registered successfully!")


def view_all_doctors():
    cursor.execute("SELECT doctor_id, name, specialization, email, phone, consultation_fee FROM doctors")
    rows = cursor.fetchall()
    if not rows:
        print("No doctors found.")
        return
    for row in rows:
        print(f"ID: {row[0]} | Name: Dr. {row[1]} | Specialization: {row[2]} | Email: {row[3]} | Phone: {row[4]} | Fee: ${row[5]}")


def search_doctor_by_id(doctor_id=None):
    if doctor_id is None:
        doctor_id = int(input("Enter Doctor ID: "))

    query = "SELECT doctor_id, name, specialization, email, phone, consultation_fee, created_at FROM doctors WHERE doctor_id = %s"
    cursor.execute(query, (doctor_id,))
    row = cursor.fetchone()

    if row is None:
        print("Doctor not found.")
        return

    print("\n--- Doctor Profile Details ---")
    print(f"ID               : {row[0]}")
    print(f"Name             : Dr. {row[1]}")
    print(f"Specialization   : {row[2]}")
    print(f"Email            : {row[3]}")
    print(f"Phone            : {row[4]}")
    print(f"Consultation Fee : ${row[5]}")
    print(f"Joined On        : {row[6]}")
    print("------------------------------\n")


def view_doctor_appointments(doctor_id):
    query = """
    SELECT a.appointment_id, p.name, a.appointment_date, a.appointment_time, a.status, a.reason_for_visit
    FROM appointments a
    JOIN patients p ON a.patient_id = p.patient_id
    WHERE a.doctor_id = %s
    ORDER BY a.appointment_date, a.appointment_time
    """
    cursor.execute(query, (doctor_id,))
    rows = cursor.fetchall()

    if not rows:
        print("No appointments found.")
        return

    print("\n--- My Appointments ---")
    for r in rows:
        print(f"Appt ID: {r[0]} | Patient: {r[1]} | Date: {r[2]} | Time: {r[3]} | Status: {r[4]} | Reason: {r[5]}")


def add_prescription(doctor_id):
    view_doctor_appointments(doctor_id)
    appt_id = int(input("Enter Appointment ID to write prescription for: "))

    cursor.execute("SELECT patient_id FROM appointments WHERE appointment_id = %s AND doctor_id = %s", (appt_id, doctor_id))
    appt_data = cursor.fetchone()

    if not appt_data:
        print("Invalid Appointment ID or appointment does not belong to you.")
        return

    patient_id = appt_data[0]
    medicines = input("Enter prescribed medicines & dosages: ")
    notes = input("Enter doctor notes: ")

    # Check if prescription exists for this appointment
    cursor.execute("SELECT * FROM prescriptions WHERE appointment_id = %s", (appt_id,))
    if cursor.fetchone() is not None:
        print("A prescription has already been issued for this appointment!")
        return

    query = "INSERT INTO prescriptions (appointment_id, doctor_id, patient_id, medicines_prescribed, doctor_notes) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (appt_id, doctor_id, patient_id, medicines, notes))
    
    # Auto-update appointment status to Completed
    cursor.execute("UPDATE appointments SET status = 'Completed' WHERE appointment_id = %s", (appt_id,))
    conn.commit()
    print("Prescription issued and appointment marked as 'Completed'!")


def update_doctor_profile(doctor_id):
    name = input("Enter updated name: ")
    specialization = input("Enter updated specialization: ")
    phone = input("Enter updated phone: ")
    fee = float(input("Enter updated consultation fee: "))

    query = "UPDATE doctors SET name = %s, specialization = %s, phone = %s, consultation_fee = %s WHERE doctor_id = %s"
    cursor.execute(query, (name, specialization, phone, fee, doctor_id))
    conn.commit()
    print("Doctor profile updated successfully!")


def delete_doctor():
    userip = int(input("Enter Doctor ID to delete: "))

    cursor.execute("SELECT * FROM doctors WHERE doctor_id = %s", (userip,))
    if cursor.fetchone() is None:
        print("Doctor ID does not exist.")
        return

    cursor.execute("DELETE FROM doctors WHERE doctor_id = %s", (userip,))
    conn.commit()
    print("Doctor deleted successfully!")
    