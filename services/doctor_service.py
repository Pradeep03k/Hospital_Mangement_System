from Database.db import connection


def register_doctor():
    conn = connection()
    cursor = conn.cursor()

    print("\n===== REGISTER DOCTOR =====")

    name = input("Doctor Name: ")
    specialization = input("Specialization: ")
    qualification = input("Qualification: ")
    mobile = input("Mobile: ")
    email = input("Email: ")
    password = input("Password: ")
    fees = float(input("Consultation Fee: "))

    sql = """
    INSERT INTO doctor
    (doctor_name, specialization, qualification, mobile, email, password, fees)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    values = (
        name,
        specialization,
        qualification,
        mobile,
        email,
        password,
        fees
    )

    cursor.execute(sql, values)
    conn.commit()

    print("\nDoctor registered successfully.")

    cursor.close()
    conn.close()


def get_all_doctors():
    conn = connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM doctor")
    doctors = cursor.fetchall()

    print("\n===== DOCTOR LIST =====")

    for doctor in doctors:
        print(doctor)

    cursor.close()
    conn.close()


def get_doctor_by_id():
    doctor_id = int(input("Enter Doctor ID: "))

    conn = connection()
    cursor = conn.cursor()

    sql = "SELECT * FROM doctor WHERE doctor_id = %s"
    cursor.execute(sql, (doctor_id,))

    doctor = cursor.fetchone()

    if doctor:
        print("\nDoctor Details:")
        print(doctor)
    else:
        print("\nDoctor not found.")

    cursor.close()
    conn.close()


def update_doctor():
    doctor_id = int(input("Enter Doctor ID: "))

    name = input("Doctor Name: ")
    specialization = input("Specialization: ")
    qualification = input("Qualification: ")
    mobile = input("Mobile: ")
    email = input("Email: ")
    fees = float(input("Consultation Fee: "))

    conn = connection()
    cursor = conn.cursor()

    sql = """
    UPDATE doctor
    SET doctor_name = %s,
        specialization = %s,
        qualification = %s,
        mobile = %s,
        email = %s,
        fees = %s
    WHERE doctor_id = %s
    """

    values = (
        name,
        specialization,
        qualification,
        mobile,
        email,
        fees,
        doctor_id
    )

    cursor.execute(sql, values)
    conn.commit()

    if cursor.rowcount > 0:
        print("\nDoctor updated successfully.")
    else:
        print("\nDoctor not found.")

    cursor.close()
    conn.close()


def delete_doctor():
    doctor_id = int(input("Enter Doctor ID: "))

    conn = connection()
    cursor = conn.cursor()

    sql = "DELETE FROM doctor WHERE doctor_id = %s"
    cursor.execute(sql, (doctor_id,))
    conn.commit()

    if cursor.rowcount > 0:
        print("\nDoctor deleted successfully.")
    else:
        print("\nDoctor not found.")

    cursor.close()
    conn.close()