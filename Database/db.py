from mysql import connector 

conn=connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hms_db"
)
print("database connected")
cursor =conn.cursor()
