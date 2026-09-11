from Database.db import conn, cursor
from models.receptionist import Receptionist


# Dynamic Receptionist Login Function
def receptionist_login():
    email = input("Enter receptionist email: ")
    password = input("Enter receptionist password: ")

    query = "SELECT receptionist_id, name, shift FROM receptionists WHERE email = %s AND password = %s"
    cursor.execute(query, (email, password))
    receptionist_record = cursor.fetchone()

    if receptionist_record is not None:
        print(f"\nLogin Successful! Welcome, {receptionist_record[1]} ({receptionist_record[2]} Shift).")
        return True
    else:
        print("\nInvalid Email or Password! Access Denied.")
        return False


# Add / Register Receptionist
def add_receptionist():
    name = input("Enter receptionist name: ")
    email = input("Enter receptionist email: ")
    password = input("Enter receptionist password: ")
    shift = input("Enter shift (Day/Night) [Default 'Day']: ")
    if shift not in ['Day', 'Night']:
        shift = 'Day'
    phone = input("Enter receptionist phone number: ")

    # Instantiate Receptionist model object
    r = Receptionist(None, name, email, password, phone, shift)

    # Check if email already exists
    cursor.execute("SELECT * FROM receptionists WHERE email = %s", (r.email,))
    if cursor.fetchone() is not None:
        print("Receptionist email already exists!")
        return

    query = "INSERT INTO receptionists (name, email, password, shift, phone) VALUES (%s, %s, %s, %s, %s)"
    values = (r.name, r.email, r.password, r.shift, r.phone)
    cursor.execute(query, values)
    conn.commit()
    print("Receptionist added successfully!")


# View All Receptionists
def view_receptionist():
    cursor.execute("SELECT receptionist_id, name, email, shift, phone FROM receptionists")
    rows = cursor.fetchall()

    if not rows:
        print("No receptionist records found.")
        return

    for i in rows:
        print(i)


# Search / View Particular Receptionist Details By ID
def search_receptionist_by_id():
    receptionist_id = int(input("Enter Receptionist ID to view details: "))

    query = "SELECT receptionist_id, name, email, shift, phone, created_at FROM receptionists WHERE receptionist_id = %s"
    cursor.execute(query, (receptionist_id,))
    row = cursor.fetchone()

    if row is None:
        print("Receptionist record not found.")
        return

    print("\n--- Receptionist Profile Details ---")
    print(f"ID         : {row[0]}")
    print(f"Name       : {row[1]}")
    print(f"Email      : {row[2]}")
    print(f"Shift      : {row[3]}")
    print(f"Phone      : {row[4]}")
    print(f"Created At : {row[5]}")
    print("------------------------------------\n")


# Update Receptionist Profile (Name, Email, Shift & Phone)
def update_receptionist():
    userip = int(input("Enter Receptionist ID to update: "))

    cursor.execute("SELECT * FROM receptionists WHERE receptionist_id = %s", (userip,))
    rows = cursor.fetchone()

    if rows is None:
        print("Receptionist ID not found.")
        return False

    name = input("Enter new name: ").strip()
    email = input("Enter new email: ").strip()
    shift = input("Enter new shift (Day/Night): ").strip().capitalize()
    if shift not in ['Day', 'Night']:
        shift = 'Day'
    phone = input("Enter new phone number: ").strip()

    query = "UPDATE receptionists SET name = %s, email = %s, shift = %s, phone = %s WHERE receptionist_id = %s"
    value = (name, email, shift, phone, userip)
    cursor.execute(query, value)
    conn.commit()
    print("Receptionist updated successfully!")


# Update Receptionist Password
def update_receptionist_password():
    userip = int(input("Enter Receptionist ID to change password: "))

    cursor.execute("SELECT * FROM receptionists WHERE receptionist_id = %s", (userip,))
    rows = cursor.fetchone()

    if rows is None:
        print("Receptionist ID not found.")
        return

    new_password = input("Enter new password: ").strip()
    query = "UPDATE receptionists SET password = %s WHERE receptionist_id = %s"
    cursor.execute(query, (new_password, userip))
    conn.commit()
    print("Receptionist password updated successfully!")


# Delete Receptionist
def delete_receptionist():
    userip = int(input("Enter Receptionist ID to delete: "))

    # Check if the receptionist exists
    cursor.execute("SELECT * FROM receptionists WHERE receptionist_id = %s", (userip,))
    rows = cursor.fetchone()

    if rows is None:
        print("Receptionist ID does not exist.")
        return

    cursor.execute("DELETE FROM receptionists WHERE receptionist_id = %s", (userip,))
    conn.commit()
    print("Receptionist deleted successfully!")