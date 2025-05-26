import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_connect"
)

if conn.is_connected():
    print("Berhasil terhubung ke database MySQL")   
    conn.close()