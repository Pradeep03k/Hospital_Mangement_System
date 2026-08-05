from mysql import connector 

conn=connector.connect(
    host="localhost",
    user="root",
    password="Enter your password",
    database="Enter your database"
)
print("database connected")
cursor =conn.cursor()
