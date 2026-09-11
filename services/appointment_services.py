from Database.db import conn, cursor

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

def view_all_appointments():
    query = """
    SELECT a.appointment_id, p.name, d.name, a.appointment_date, a.appointment_time, a.status, a.reason_for_visit
    FROM appointments a
    JOIN patients p ON a.patient_id = p.patient_id
    JOIN doctors d ON a.doctor_id = d.doctor_id
    ORDER BY a.appointment_date DESC
    """
    cursor.execute(query)
    rows = cursor.fetchall()

    if not rows:
        print("No appointments found.")
        return

    print("\n--- All System Appointments ---")
    for r in rows:
        print(f"Appt ID: {r[0]} | Patient: {r[1]} | Doctor: Dr. {r[2]} | Date: {r[3]} {r[4]} | Status: {r[5]}")


def update_appointment_status():
    appt_id = int(input("Enter Appointment ID: "))

    cursor.execute("SELECT * FROM appointments WHERE appointment_id = %s", (appt_id,))
    if cursor.fetchone() is None:
        print("Appointment ID not found.")
        return

    print("Status Options: 1. Confirmed | 2. Completed | 3. Cancelled")
    choice = input("Select new status (1-3): ")

    status_map = {'1': 'Confirmed', '2': 'Completed', '3': 'Cancelled'}
    new_status = status_map.get(choice)

    if not new_status:
        print("Invalid choice.")
        return

    query = "UPDATE appointments SET status = %s WHERE appointment_id = %s"
    cursor.execute(query, (new_status, appt_id))
    conn.commit()
    print(f"Appointment ID {appt_id} updated to status: {new_status}!")

# Delete Appointment Function (Supports both Admin/Receptionist and Patient)
def delete_appointment(patient_id=None):
    print("\n================ DELETE APPOINTMENT ================")
    appt_id = int(input("Enter Appointment ID to delete: "))

    # Case 1: Called by Patient (Check if appointment belongs specifically to this logged-in patient)
    if patient_id is not None:
        query = """
        SELECT a.appointment_id, d.name, a.appointment_date, a.appointment_time 
        FROM appointments a
        JOIN doctors d ON a.doctor_id = d.doctor_id
        WHERE a.appointment_id = %s AND a.patient_id = %s
        """
        cursor.execute(query, (appt_id, patient_id))
        record = cursor.fetchone()

        if record is None:
            print(f"[Error] Appointment ID {appt_id} not found under your account. Deletion denied.")
            return

        confirm = input(f"Are you sure you want to cancel/delete your appointment with Dr. {record[1]} on {record[2]}? (y/n): ")
        if confirm == 'y':
            cursor.execute("DELETE FROM appointments WHERE appointment_id = %s AND patient_id = %s", (appt_id, patient_id))
            conn.commit()
            print(f"\n[Success] Appointment ID {appt_id} has been deleted successfully.")
        else:
            print("\nDeletion cancelled.")

    # Case 2: Called by Admin / Receptionist (Can delete any appointment by ID)
    else:
        query = """
        SELECT a.appointment_id, p.name, d.name, a.appointment_date, a.appointment_time 
        FROM appointments a
        JOIN patients p ON a.patient_id = p.patient_id
        JOIN doctors d ON a.doctor_id = d.doctor_id
        WHERE a.appointment_id = %s
        """
        cursor.execute(query, (appt_id,))
        record = cursor.fetchone()

        if record is None:
            print(f"[Error] Appointment ID {appt_id} not found in the system.")
            return

        print(f"\n--- Appointment Details ---")
        print(f"Patient Name : {record[1]}")
        print(f"Doctor Name  : Dr. {record[2]}")
        print(f"Date & Time  : {record[3]} at {record[4]}")

        confirm = input(f"\nAre you sure you want to delete Appointment ID {appt_id}? (y/n): ")
        if confirm == 'y':
            cursor.execute("DELETE FROM appointments WHERE appointment_id = %s", (appt_id,))
            conn.commit()
            print(f"\n[Success] Appointment ID {appt_id} has been permanently deleted.")
        else:
            print("\nDeletion cancelled by staff.")