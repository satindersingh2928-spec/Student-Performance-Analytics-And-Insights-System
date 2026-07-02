import mysql.connector
from config import DB_CONFIG
import time

def get_connection():
    try:
        start = time.time()

        conn = mysql.connector.connect(
            host=DB_CONFIG.get("host"),
            user=DB_CONFIG.get("user"),
            password=DB_CONFIG.get("password"),
            database=DB_CONFIG.get("database"),
            port=DB_CONFIG.get("port"),
            ssl_ca=DB_CONFIG.get("ssl_ca") or None
        )

        print(f"[DB] Connected in {time.time() - start:.2f} sec")

        return conn

    except mysql.connector.Error as err:
        print(f"[DB ERROR] {err}")
        return None
    
def log_activity(username, action, description):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

    INSERT INTO activity_logs(

        username,
        action,
        description

    )

    VALUES(%s,%s,%s)

    """,

    (

        username,
        action,
        description

    )

    )

    conn.commit()

    cursor.close()
    conn.close()
    
def get_total_students(cursor):

    cursor.execute(
        "SELECT COUNT(*) FROM students"
    )

    return cursor.fetchone()[0]

def get_average_percentage(cursor):

    cursor.execute(
        "SELECT ROUND(AVG(percentage),2) FROM students"
    )

    return cursor.fetchone()[0]

def get_average_attendance(cursor):

    cursor.execute("""
        SELECT ROUND(AVG(attendance_percentage),2)
        FROM students
    """)

    return cursor.fetchone()[0]

def get_pass_count(cursor):

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM students
        WHERE percentage >= 40
        """
    )

    return cursor.fetchone()[0]

def get_fail_count(cursor):

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM students
        WHERE percentage < 40
        """
    )

    return cursor.fetchone()[0]

def get_highest_attendance_student(cursor):

    cursor.execute("""
        SELECT student_name, attendance_percentage
        FROM students
        ORDER BY attendance_percentage DESC
        LIMIT 1
    """)

    return cursor.fetchone()

def get_lowest_attendance_student(cursor):

    cursor.execute("""
        SELECT student_name, attendance_percentage
        FROM students
        ORDER BY attendance_percentage ASC
        LIMIT 1
    """)

    return cursor.fetchone()

def get_top_performers(cursor):

    cursor.execute("""
        SELECT student_name, percentage
        FROM students
        ORDER BY percentage DESC
        LIMIT 5
    """)

    return cursor.fetchall()

def get_bottom_performers(cursor):

    cursor.execute("""
        SELECT student_name, percentage
        FROM students
        ORDER BY percentage ASC
        LIMIT 5
    """)

    return cursor.fetchall()