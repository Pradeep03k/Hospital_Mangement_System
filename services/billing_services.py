from Database.db import conn, cursor
from models.billing import Billing


def create_bill():
    patient_id = int(input("Enter Patient ID: "))
    
    # Optional linked appointment
    appt_input = input("Enter Appointment ID (Press Enter to skip): ")
    appointment_id = int(appt_input) if appt_input else None

    # get consultation fee if appointment ID is provided
    default_amount = 0.0
    if appointment_id:
        cursor.execute("""
            SELECT d.consultation_fee 
            FROM appointments a 
            JOIN doctors d ON a.doctor_id = d.doctor_id 
            WHERE a.appointment_id = %s
        """, (appointment_id,))
        fee_data = cursor.fetchone()
        if fee_data:
            default_amount = float(fee_data[0])

    amount_input = input(f"Enter total bill amount (Default INR{default_amount}): ")
    total_amount = float(amount_input) if amount_input else default_amount

    payment_method = input("Enter payment method (Cash/Card/UPI) [Default Cash]: ")
    if not payment_method:
        payment_method = "Cash"

    bill = Billing(patient_id, total_amount, appointment_id, "Unpaid", payment_method)

    query = """
    INSERT INTO billing (patient_id, appointment_id, total_amount, payment_status, payment_method)
    VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(query, (bill.patient_id, bill.appointment_id, bill.total_amount, bill.payment_status, bill.payment_method))
    conn.commit()
    print("Bill invoice created successfully!")


def view_all_bills():
    query = """
    SELECT b.bill_id, p.name, b.appointment_id, b.total_amount, b.payment_status, b.payment_method, b.billing_date
    FROM billing b
    JOIN patients p ON b.patient_id = p.patient_id
    ORDER BY b.billing_date DESC
    """
    cursor.execute(query)
    rows = cursor.fetchall()

    if not rows:
        print("No billing records found.")
        return

    print("\n--- Hospital Billing Records ---")
    for r in rows:
        print(f"Bill ID: {r[0]} | Patient: {r[1]} | Appt ID: {r[2]} | Amount: ${r[3]} | Status: {r[4]} | Method: {r[5]} | Date: {r[6]}")


def process_payment():
    bill_id = int(input("Enter Bill ID to collect payment: "))

    cursor.execute("SELECT * FROM billing WHERE bill_id = %s", (bill_id,))
    bill = cursor.fetchone()

    if not bill:
        print("Bill ID not found.")
        return

    method = input("Select payment method (Cash/Card/UPI): ")
    query = "UPDATE billing SET payment_status = 'Paid', payment_method = %s WHERE bill_id = %s"
    cursor.execute(query, (method, bill_id))
    conn.commit()
    print(f"Payment received! Bill ID {bill_id} marked as 'Paid'.")


def view_patient_bills(patient_id):
    query = "SELECT bill_id, appointment_id, total_amount, payment_status, payment_method, billing_date FROM billing WHERE patient_id = %s"
    cursor.execute(query, (patient_id,))
    rows = cursor.fetchall()

    if not rows:
        print("No bill records found for this patient.")
        return

    print("\n--- My Invoices & Bills ---")
    for r in rows:
        print(f"Bill ID: {r[0]} | Appt ID: {r[1]} | Amount: ${r[2]} | Status: {r[3]} | Method: {r[4]} | Date: {r[5]}")

# Admin Feature: Delete a specific bill for a particular patient
def delete_patient_bill_admin():
    print("\n================ ADMIN: DELETE PATIENT BILL ================")
    patient_id = int(input("Enter Patient ID: "))

    # Check if patient exists and view their bills first
    cursor.execute("""
        SELECT b.bill_id, b.appointment_id, b.total_amount, b.payment_status, b.billing_date 
        FROM billing b
        WHERE b.patient_id = %s
    """, (patient_id,))
    patient_bills = cursor.fetchall()

    if not patient_bills:
        print(f"No billing records found for Patient ID {patient_id}.")
        return

    print(f"\n--- Invoices Linked to Patient ID {patient_id} ---")
    for bill in patient_bills:
        print(f"Bill ID: {bill[0]} | Appt ID: {bill[1]} | Amount: INR {bill[2]} | Status: {bill[3]} | Date: {bill[4]}")
    print("---------------------------------------------------------")

    bill_id = int(input("\nEnter specific Bill ID to delete: "))

    # Verify that the specified bill exists and actually belongs to the given patient
    cursor.execute("SELECT bill_id, total_amount FROM billing WHERE bill_id = %s AND patient_id = %s", (bill_id, patient_id))
    record = cursor.fetchone()

    if record is None:
        print(f"\n[Error] Invalid Bill ID {bill_id} for Patient ID {patient_id}. Deletion cancelled.")
        return

    # Deletion confirmation step
    confirm = input(f"Are you sure you want to permanently delete Bill ID {bill_id} (Amount: INR {record[1]})? (yes/no): ")
    if confirm == 'y':
        cursor.execute("DELETE FROM billing WHERE bill_id = %s AND patient_id = %s", (bill_id, patient_id))
        conn.commit()
        print(f"\n[Success] Bill ID {bill_id} for Patient ID {patient_id} has been permanently deleted.")
    else:
        print("\nDeletion cancelled by Admin.")

# Receptionist Feature: Update Bill details if added incorrectly by mistake
def update_bill():
    print("\n================ RECEPTIONIST: UPDATE BILL DETAILS ================")
    bill_id = int(input("Enter Bill ID to update/correct: "))

    # Check if Bill exists
    cursor.execute("""
        SELECT b.bill_id, p.name, b.appointment_id, b.total_amount, b.payment_status, b.payment_method
        FROM billing b
        JOIN patients p ON b.patient_id = p.patient_id
        WHERE b.bill_id = %s
    """, (bill_id,))
    bill = cursor.fetchone()

    if bill is None:
        print(f"[Error] Bill ID {bill_id} not found.")
        return

    print(f"\n--- Current Bill Details ---")
    print(f"Bill ID        : {bill[0]}")
    print(f"Patient Name   : {bill[1]}")
    print(f"Appointment ID : {bill[2]}")
    print(f"Total Amount   : INR {bill[3]}")
    print(f"Payment Status : {bill[4]}")
    print(f"Payment Method : {bill[5]}")
    print("--------------------------------")

    print("\nEnter new details (Press ENTER to keep the current value):")
    
    # Optional updates with default fallback to current values
    new_amount_input = input(f"New Total Amount (Current: INR {bill[3]}): ").strip()
    new_amount = float(new_amount_input) if new_amount_input else float(bill[3])

    new_status = input(f"New Payment Status (Paid/Unpaid) (Current: {bill[4]}): ").strip()
    if not new_status:
        new_status = bill[4]

    new_method = input(f"New Payment Method (Cash/Card/UPI) (Current: {bill[5]}): ").strip()
    if not new_method:
        new_method = bill[5]

    # Execute Update query
    update_query = """
    UPDATE billing 
    SET total_amount = %s, payment_status = %s, payment_method = %s 
    WHERE bill_id = %s
    """
    cursor.execute(update_query, (new_amount, new_status, new_method, bill_id))
    conn.commit()

    print(f"\n[Success] Bill ID {bill_id} has been updated successfully!")