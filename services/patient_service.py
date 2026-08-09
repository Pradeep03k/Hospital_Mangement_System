from Database.db import conn, cursor
from models.patient import Patient


# Add / Register Patient
def add_patient():
    name = input("Enter patient name: ").strip()
    email = input("Enter patient email: ").strip()
    password = input("Enter patient password: ").strip()
    phone = input("Enter patient phone number: ").strip()
    age = int(input("Enter patient age: "))
    gender = input("Enter patient gender (Male/Female/Other): ").strip().capitalize()

    if gender not in ["Male", "Female", "Other"]:
        gender = "Other"

    address = input("Enter patient address: ").strip()

    # Create Patient Object
    p = Patient(None, name, email, password, phone, age, gender, address)

    # Check Email Already Exists
    cursor.execute("SELECT * FROM patients WHERE email = %s", (p.email,))
    if cursor.fetchone() is not None:
        print("Patient email already exists!")
        return

    query = """
    INSERT INTO patients(name, email, password, phone, age, gender, address)
    VALUES(%s, %s, %s, %s, %s, %s, %s)
    """

    values = (
        p.name,
        p.email,
        p.password,
        p.phone,
        p.age,
        p.gender,
        p.address
    )

    cursor.execute(query, values)
    conn.commit()

    print("Patient added successfully!")


# View All Patients
def view_patient():
    cursor.execute("""
    SELECT patient_id, name, email, password, phone, age, gender, address, created_at
    FROM patients
    """)

    rows = cursor.fetchall()

    if not rows:
        print("No patient records found.")
        return

    for row in rows:
        print(row)


# Search Patient By ID
def search_patient_by_id():
    patient_id = int(input("Enter Patient ID: "))

    query = """
    SELECT patient_id, name, email, password, phone, age, gender, address, created_at
    FROM patients
    WHERE patient_id = %s
    """

    cursor.execute(query, (patient_id,))
    row = cursor.fetchone()

    if row is None:
        print("Patient record not found.")
        return

    print("\n------ Patient Details ------")
    print(f"ID         : {row[0]}")
    print(f"Name       : {row[1]}")
    print(f"Email      : {row[2]}")
    print(f"Password   : {row[3]}")
    print(f"Phone      : {row[4]}")
    print(f"Age        : {row[5]}")
    print(f"Gender     : {row[6]}")
    print(f"Address    : {row[7]}")
    print(f"Created At : {row[8]}")
    print("-----------------------------")


# Update Patient
def update_patient():
    userip = int(input("Enter Patient ID to update: "))

    cursor.execute("SELECT * FROM patients WHERE patient_id = %s", (userip,))
    rows = cursor.fetchone()

    if rows is None:
        print("Patient ID not found.")
        return

    name = input("Enter new name: ").strip()
    email = input("Enter new email: ").strip()
    phone = input("Enter new phone number: ").strip()
    age = int(input("Enter new age: "))
    gender = input("Enter new gender (Male/Female/Other): ").strip().capitalize()

    if gender not in ["Male", "Female", "Other"]:
        gender = "Other"

    address = input("Enter new address: ").strip()

    # Check Duplicate Email
    cursor.execute(
        "SELECT * FROM patients WHERE email = %s AND patient_id != %s",
        (email, userip)
    )

    if cursor.fetchone() is not None:
        print("Patient email already exists!")
        return

    query = """
    UPDATE patients
    SET name=%s,
        email=%s,
        phone=%s,
        age=%s,
        gender=%s,
        address=%s
    WHERE patient_id=%s
    """

    values = (
        name,
        email,
        phone,
        age,
        gender,
        address,
        userip
    )

    cursor.execute(query, values)
    conn.commit()

    print("Patient updated successfully!")


# Update Patient Password
def update_patient_password():
    userip = int(input("Enter Patient ID to change password: "))

    cursor.execute("SELECT * FROM patients WHERE patient_id = %s", (userip,))
    rows = cursor.fetchone()

    if rows is None:
        print("Patient ID not found.")
        return

    new_password = input("Enter new password: ").strip()

    query = "UPDATE patients SET password = %s WHERE patient_id = %s"

    cursor.execute(query, (new_password, userip))
    conn.commit()

    print("Patient password updated successfully!")


# Delete Patient
def delete_patient():
    userip = int(input("Enter Patient ID to delete: "))

    cursor.execute("SELECT * FROM patients WHERE patient_id = %s", (userip,))
    rows = cursor.fetchone()

    if rows is None:
        print("Patient ID does not exist.")
        return

    cursor.execute("DELETE FROM patients WHERE patient_id = %s", (userip,))
    conn.commit()

    print("Patient deleted successfully!")