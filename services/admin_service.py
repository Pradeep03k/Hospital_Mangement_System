from Database.db import conn, cursor
from models.admin import Admin

# Dynamic Admin Login Function
def admin_login():
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")

    query = "SELECT admin_id, username, email FROM admin WHERE username = %s AND password = %s"
    values=(username,password)
    cursor.execute(query,values)
    admin_record = cursor.fetchone()

    if admin_record is not None:
        print(f"\nLogin Successful! Welcome, {admin_record[1]}.")
        return True  # Login succeeded dynamically against DB records
    else:
        print("\nInvalid Username or Password! Access Denied.")
        return False  # Login failed


# Add / Register Admin
def add_admin():
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")
    email = input("Enter admin email: ")
    
    #Admin object from model
    a = Admin(username, password, email)
    
    # Check if username or email already exists
    cursor.execute("SELECT * FROM admin WHERE username = %s OR email = %s", (a.username, a.email))
    if cursor.fetchone() is not None:
        print("Admin username or email already exists!")
        return

    query = "INSERT INTO admin (username, password, email) VALUES (%s, %s, %s)"
    values = (a.username, a.password, a.email)
    cursor.execute(query, values)
    conn.commit()
    print("Admin added successfully!")


# View All Admins
def view_admin():
    cursor.execute("SELECT admin_id, username, email, created_at FROM admin")
    rows = cursor.fetchall()

    if not rows:
        print("Record not found")
        return

    for i in rows:
        print(i)


# Search / View Particular Admin Details By ID
def search_admin_by_id():
    admin_id = int(input("Enter your Admin ID to view details: "))
    
    query = "SELECT admin_id, username, email, created_at FROM admin WHERE admin_id = %s"
    values=(admin_id,)
    cursor.execute(query,values)
    row = cursor.fetchone()
    
    if row is None:
        print("Admin record not found.")
        return

    print("\n--- Admin Profile Details ---")
    print(f"ID         : {row[0]}")
    print(f"Username   : {row[1]}")
    print(f"Email      : {row[2]}")
    print(f"Created At : {row[3]}")
    print("-----------------------------\n")


# Update Admin Profile
def update_admin():
    userip = int(input("Enter admin ID: "))
    
    cursor.execute("SELECT * FROM admin WHERE admin_id = %s", (userip,))
    rows = cursor.fetchone()
    
    if rows is None:
        print("Admin ID not found.")
        return False

    username = input("Enter new admin username: ")
    email = input("Enter new admin email: ")
    
    query = "UPDATE admin SET username = %s, email = %s WHERE admin_id = %s"
    value = (username, email, userip)
    cursor.execute(query, value)
    conn.commit()
    print("Admin updated successfully!")


# Update Admin Password
def update_admin_password():
    userip = int(input("Enter admin ID to change password: "))
    
    cursor.execute("SELECT * FROM admin WHERE admin_id = %s", (userip,))
    rows = cursor.fetchone()
    
    if rows is None:
        print("Admin ID not found.")
        return

    new_password = input("Enter new password: ")
    query = "UPDATE admin SET password = %s WHERE admin_id = %s"
    values=(new_password, userip)
    cursor.execute(query, values)
    conn.commit()
    print("Admin password updated successfully!")


# Delete Admin
def delete_admin():
    userip = int(input("Enter admin ID to delete: "))
    
    # Check if the admin exists
    cursor.execute("SELECT * FROM admin WHERE admin_id = %s", (userip,))
    rows = cursor.fetchone()
    
    if rows is None:
        print("Admin ID does not exist.")
        return
    cursor.execute("SELECT COUNT(*) FROM admin")  #system have at least one admin so i make that logic 
    total_admins = cursor.fetchone()[0]  
    if total_admins <= 1:
        print("Can't delete this admin! System must have at least one active admin.")
        return
    cursor.execute("DELETE FROM admin WHERE admin_id = %s", (userip,))
    conn.commit()
    print("Admin deleted successfully...!")