from flask import Flask
import mysql.connector
import os
app = Flask(__name__)

@app.route("/")
def home():
    conn = mysql.connector.connect(
        host="localhost",
        user="appuser",
        password=os.getenv("DB_PASSWORD"),
        database="studentdb"
    )

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return f"Students: {rows}"

app.run(host="0.0.0.0", port=5000)
