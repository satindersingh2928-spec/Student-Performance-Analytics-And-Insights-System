import mysql.connector
import random

from werkzeug.security import generate_password_hash

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="student_performance_analytics"
)

cursor = conn.cursor()

courses = {
    "BCA": [
        "Computer Science",
        "Data Science",
        "AI & ML"
    ],

    "MCA": [
        "Software Development",
        "Cloud Computing",
        "Data Science"
    ],

    "BTech": [
        "AI & DS",
        "Cyber Security",
        "Cloud Computing",
        "IT"
    ],

    "MBA": [
        "Finance",
        "Marketing",
        "HR",
        "Business Analytics"
    ],

    "BBA": [
        "General",
        "Finance",
        "Marketing"
    ],

    "BSc": [
        "Computer Science",
        "Mathematics",
        "Physics"
    ],

    "BA": [
        "English",
        "Economics",
        "History"
    ]
}

cities = [
    "Mumbai",
    "Delhi",
    "Pune",
    "Bangalore",
    "Hyderabad",
    "Jaipur",
    "Ahmedabad",
    "Chennai",
    "Lucknow",
    "Indore",
    "Kota",
    "Chandigarh",
    "Amritsar",
    "Alwar"
]

male_names = [
    "Rahul",
    "Aman",
    "Rohit",
    "Karan",
    "Vikas",
    "Arjun",
    "Saurabh",
    "Ayush",
    "Satinder",
    "Shivraj",
    "Nikhil",
    "Devraj",
    "Vishwas",
    "Madhva",
    "Manoj",
    "Umesh",
    "Shyam",
    "Vivek",
    "Ritik",
    "Ajay",
    "Shubham",
    "Arun",
    "Micky",
    "Chetan",
    "Kanishk",
    "Naman",
    "Pankaj",
    "Vinayak",
    "Hardik",
    "Kunal",
    "Sumit",
    "Bhavesh",
    "Punit",
    "Yash",
    "Aditya"
]

female_names = [
    "Priya",
    "Sneha",
    "Anjali",
    "Pooja",
    "Neha",
    "Riya",
    "Nisha",
    "Muskan",
    "Palak",
    "Shreya",
    "Mahima",
    "Ritika",
    "Nikita",
    "Shivangi",
    "Prabhjot",
    "Radhika",
    "Malti",
    "Meenakshi",
    "Tanu",
    "Shalini",
    "Priyal",
    "Zoya",
    "Janvi",
    "Khushi",
    "Payal",
    "Tamanna",
    "Vinita",
    "Archi",
    "Sanjana",
    "Anisha",
    "Sneha",
    "Nikunj",
    "Shruti",
    "Preeti",
    "Vanshika",
    "Aditi",
]

last_names = [
    "Verma",
    "Patel",
    "Gupta",
    "Yadav",
    "Joshi",
    "Mishra",
    "Jain",
    "Agarwal",
    "Singh",
    "Shekhawat",
    "Garg",
    "Singh",
    "Sharma",
    "Kumar",
    "Chauhan",
    "Prajapat",
    "Pandey",
    "Neel",
    "Meena",
    "Maan",
    "Kang",
    "Sandhu",
    "Yogi",
    "Rajawat",
    "Dhariwal",
    "Yadav",
    "Barman",
    "Gill",
    "Kohli",
    "Kalra"
]

def generate_registration_no(number):
    return f"SPAI{number:04d}"

def generate_student_name(gender):

    if gender == "Male":
        first_name = random.choice(male_names)
    else:
        first_name = random.choice(female_names)

    last_name = random.choice(last_names)

    return f"{first_name} {last_name}"

def generate_gender():
    return random.choice(
        ["Male", "Female"]
    )

def generate_age():
    return random.randint(18, 25)

def generate_course_and_specialization():

    course = random.choice(
        list(courses.keys())
    )

    specialization = random.choice(
        courses[course]
    )

    return course, specialization

def generate_year(course):

    if course == "BTech":
        return random.randint(1, 4)

    elif course in ["MBA", "MCA"]:
        return random.randint(1, 2)

    else:
        return random.randint(1, 3)

def generate_semester(year):

    return random.choice(
        [
            (year * 2) - 1,
            year * 2
        ]
    )
    
def generate_city():
    return random.choice(cities)

def generate_marks(student_type):

    if student_type == "top":

        assignment = round(
            random.uniform(9, 10), 2
        )

        internal = round(
            random.uniform(13, 15), 2
        )

        practical = round(
            random.uniform(13, 15), 2
        )

        final_exam = round(
            random.uniform(54, 60), 2
        )

    elif student_type == "average":

        assignment = round(
            random.uniform(6, 9), 2
        )

        internal = round(
            random.uniform(9, 13), 2
        )

        practical = round(
            random.uniform(9, 13), 2
        )

        final_exam = round(
            random.uniform(36, 54), 2
        )

    elif student_type == "weak":

        assignment = round(
            random.uniform(4, 6), 2
        )

        internal = round(
            random.uniform(6, 9), 2
        )

        practical = round(
            random.uniform(6, 9), 2
        )

        final_exam = round(
            random.uniform(24, 36), 2
        )

    else:

        assignment = round(
            random.uniform(0, 4), 2
        )

        internal = round(
            random.uniform(0, 6), 2
        )

        practical = round(
            random.uniform(0, 6), 2
        )

        final_exam = round(
            random.uniform(0, 24), 2
        )

    total_marks = (
        assignment +
        internal +
        practical +
        final_exam
    )

    percentage = total_marks

    return (
        assignment,
        internal,
        practical,
        final_exam,
        total_marks,
        percentage
    )
    
def generate_grade(percentage):

    if percentage >= 90:
        return "O"

    elif percentage >= 80:
        return "A+"

    elif percentage >= 70:
        return "A"

    elif percentage >= 60:
        return "B+"

    elif percentage >= 50:
        return "B"

    elif percentage >= 40:
        return "C"

    else:
        return "F"
    
student_number = 1

student_categories = (
    ["top"] * 50 +
    ["average"] * 180 +
    ["weak"] * 80 +
    ["risk"] * 40
)

random.shuffle(student_categories)

for student_type in student_categories:

    registration_no = generate_registration_no(
        student_number
    )

    gender = generate_gender()

    student_name = generate_student_name(gender)

    age = generate_age()

    city = generate_city()

    course, specialization = (
        generate_course_and_specialization()
    )

    year = generate_year(course)

    semester = generate_semester(year)

    attendance = round(
        random.uniform(35, 100),
        2
    )

    (
        assignment,
        internal,
        practical,
        final_exam,
        total_marks,
        percentage
    ) = generate_marks(student_type)

    grade = generate_grade(percentage)

    student_query = """
    INSERT INTO students
    (
        registration_no,
        student_name,
        gender,
        age,
        city,
        course,
        specialization,
        year,
        semester,
        attendance_percentage,
        assignment_marks,
        internal_marks,
        practical_marks,
        final_exam_marks,
        total_marks,
        percentage,
        grade
    )
    VALUES
    (
        %s,%s,%s,%s,%s,
        %s,%s,%s,%s,
        %s,%s,%s,%s,%s,
        %s,%s,%s
    )
    """

    cursor.execute(
        student_query,
        (
            registration_no,
            student_name,
            gender,
            age,
            city,
            course,
            specialization,
            year,
            semester,
            attendance,
            assignment,
            internal,
            practical,
            final_exam,
            total_marks,
            percentage,
            grade
        )
    )

    student_id = cursor.lastrowid

    hashed_password = generate_password_hash(
        "student123"
    )

    user_query = """
    INSERT INTO users
    (
        username,
        password,
        role,
        student_id
    )
    VALUES
    (
        %s,
        %s,
        'student',
        %s
    )
    """

    cursor.execute(
        user_query,
        (
            registration_no,
            hashed_password,
            student_id
        )
    )

    student_number += 1
    
conn.commit()

cursor.close()

conn.close()

print("350 Students Generated Successfully")