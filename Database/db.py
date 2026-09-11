from mysql import connector 

conn=connector.connect(
    host="localhost",
    user="root",
    password="242003",
    database="hms_db"
)
print("database connected")
cursor =conn.cursor()
