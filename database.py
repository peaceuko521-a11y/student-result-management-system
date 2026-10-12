import sqlite3

# Connect to the database
connection = sqlite3.connect('students.db')

cursor = connection.cursor()

#STUDENTS TABLE

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    matric_number TEXT UNIQUE NOT NULL,
    department TEXT NOT NULL,
    level INTEGER NOT NULL
)
""")
#
# RESULTS TABLE
#
cursor.execute("""
CREATE TABLE IF NOT EXISTS results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    matric_number TEXT NOT NULL,
    semester TEXT NOT NULL,
    course_code TEXT NOT NULL,
    course_title TEXT NOT NULL,
    units INTEGER NOT NULL,
    score INTEGER NOT NULL,
    grade TEXT NOT NULL,
    grade_point INTEGER NOT NULL,
    FOREIGN KEY (matric_number) REFERENCES students (matric_number)
)
""")
cursor.execute("""
CREATE UNIQUE INDEX IF NOT EXISTS unique_student_course
ON results (matric_number, semester, course_code)
""")


# 13 STUDENTS 

students = [
    ("Ayodele Idris", "ART/25/26/0010", "Fine Arts", 200),
    ("Ayomide Blessing", "ART/25/26/0012", "Fine Arts", 200),
    ("Chigozie Favour", "LAW/26/27/0037", "Law", 100),
    ("Etim Nancy", "EES/24/25/0125", "Mechanical Engineering", 300),
    ("Eze Austin", "CSC/26/27/0273", "Computer Science", 100),
    ("Faustina Jones", "ECO/26/27/0324", "Economics", 100),
    ("Janet Bassey", "EES/26/27/0496", "Mechanical Engineering", 100),
    ("Kabirat Umar", "ARC/23/24/0499", "Architecture", 400),
    ("Ola Charles", "ECO/26/27/0721", "Economics", 100),
    ("Olamide Steven", "CSC/26/27/0725", "Computer Science", 100),
    ("Oscar Benjamin", "MLS/24/25/0831", "Medical Laboratory Science", 300),
    ("Rabiu Bola", "ECO/26/27/0862", "Economics", 100),
    ("Udoh David", "ARC/26/27/0887", "Architecture", 100),
]

# Insert students
cursor.executemany("""
    INSERT OR IGNORE INTO students (name, matric_number, department, level)
    VALUES(?, ?, ?, ?) """, students)


#RESULTS

results = [
    
    #Ayodele Idris
    
    ("ART/25/26/0010", "1st Semester", "ART 201", "Basic Drawing", 3, 85,"A", 5),
    ("ART/25/26/0010", "1st Semester", "ART 211", "Art Appreciation", 2, 75, "A", 5),
    ("ART/25/26/0010", "1st Semester", "ART 242", "Painting", 3, 65, "B", 4),
    ("ART/25/26/0010", "1st Semester", "ART 282", "Sculpture", 2, 55, "C", 3),
    ("ART/25/26/0010", "1st Semester", "ART 251", "Graphic Design", 3, 59, "C", 3),

    #Ayomide Blessing

    ("ART/25/26/0012", "1st Semester", "ART 201", "Basic Drawing", 3, 70, "A", 5),
    ("ART/25/26/0012", "1st Semester", "ART 211", "Art Appreciation", 2, 50, "C", 3),
    ("ART/25/26/0012", "1st Semester", "ART 242", "Painting", 3, 41, "E", 1),
    ("ART/25/26/0012", "1st Semester", "ART 282", "Sculpture", 2, 65, "B", 4),
    ("ART/25/26/0012", "1st Semester", "ART 251", "Graphic Design", 3, 32, "F", 0),

    #Chigozie Favour
    ("LAW/26/27/0037", "1st Semester", "LAW 101", "Introduction to Law", 3, 75, "A", 5),
    ("LAW/26/27/0037", "1st Semester", "LAW 102", "Legal Writing", 2, 49, "D", 2),
    ("LAW/26/27/0037", "1st Semester", "PSY 101", "Introduction To Psychology", 3, 55, "C", 3),
    ("LAW/26/27/0037", "1st Semester", "POL 101", "Legal Methods", 2, 45, "D", 2),
    ("LAW/26/27/0037", "1st Semester", "GST 111", "Communication In English", 3, 35, "F", 0),

    #Eim Nancy
    ("EES/24/25/0125", "1st Semester", "GET 101", "Introduction to Engineering", 3, 95, "A", 5),
    ("EES/24/25/0125", "1st Semester", "CHM 101", "General Chemistry", 2, 70, "A", 5),
    ("EES/24/25/0125", "1st Semester", "MTH 101", "Elementary Mathematics", 3, 67, "B", 4),
    ("EES/24/25/0125", "1st Semester", "PHY 101", "General Physics", 2, 80, "A", 5),
    ("EES/24/25/0125", "1st Semester", "GST 111", "Communication In English", 3, 72, "A", 5),

    #Eze Austin
    ("CSC/26/27/0273", "1st Semester", "COS 101", "Introduction to Computer Science", 3, 85, "A", 5),
    ("CSC/26/27/0273", "1st Semester", "GST 111", "Communication In English", 2, 65, "B", 4),
    ("CSC/26/27/0273", "1st Semester", "COS 242", "Data Structures", 3, 69, "B", 4),
    ("CSC/26/27/0273", "1st Semester", "STA 111", "Descriptive Statistics", 2, 45, "D", 2),
    ("CSC/26/27/0273", "1st Semester", "MTH 101", "Elementary Mathematics", 3, 35, "F", 0),

    #Faustina Jones
    ("ECO/26/27/0324", "1st Semester", "ECO 101", "Principles Of Economics", 3, 80, "A", 5),
    ("ECO/26/27/0324", "1st Semester", "SOC 101", "Introduction to Sociology", 2, 70, "A", 5),
    ("ECO/26/27/0324", "1st Semester", "POL 101", "Introduction To Political Science", 3, 60, "B", 4),
    ("ECO/26/27/0324", "1st Semester", "GST 111", "Communication In English", 2, 50, "C", 3),
    ("ECO/26/27/0324", "1st Semester", "ECO 103", "Development Economics", 3, 40, "D", 2),

    #Janet Bassey
    ("EES/26/27/0496", "1st Semester", "GST 111", "Communication In English", 3, 72, "A", 5),
    ("EES/26/27/0496", "1st Semester", "GET 101", "Introduction to Engineering", 2, 95, "A", 5),
    ("EES/26/27/0496", "1st Semester", "CHM 101", "General Chemistry", 3, 47, "D", 2),
    ("EES/26/27/0496", "1st Semester", "MTH 101", "Elementary Mathematics", 2, 67, "B", 4),
    ("EES/26/27/0496", "1st Semester", "PHY 101", "General Physics", 2, 80, "A", 5),

    #Kabirat Umar
    ("ARC/23/24/0499", "1st Semester", "ARC 409", "Research Methods In Architecture", 3, 35, "F", 0),
    ("ARC/23/24/0499", "1st Semester", "ARC 407", "Tourism And Research Planning Theory", 3, 42, "E", 1),
    ("ARC/23/24/0499", "1st Semester", "ARC 405", "Working Drawings And Construction Methods", 2, 75, "B", 4),
    ("ARC/23/24/0499", "1st Semester", "URP 408", "Rural Planning And Sustainable Settlement Design", 3, 80, "A", 5),
    ("ARC/23/24/0499", "1st Semester", "ARC 403", "Building Components And Construction Methods", 2, 62, "B", 4),

    #Ola Charles
    ("ECO/26/27/0721", "1st Semester", "ECO 101", "Principles Of Economics", 3, 80, "A", 5),
    ("ECO/26/27/0721", "1st Semester", "SOC 101", "Introduction to Sociology", 2, 70, "A", 5),
    ("ECO/26/27/0721", "1st Semester", "POL 101", "Introduction To Political Science", 3, 60, "B", 4),
    ("ECO/26/27/0721", "1st Semester", "GST 111", "Communication In English", 2, 50, "C", 3),
    ("ECO/26/27/0721", "1st Semester", "ECO 103", "Development Economics", 3, 40, "D", 2),

    #Olamide Steven
    ("CSC/26/27/0725", "1st Semester", "COS 101", "Introduction to Computer Science", 3, 85, "A", 5),
    ("CSC/26/27/0725", "1st Semester", "GST 111", "Communication In English", 2, 65, "B", 4),
    ("CSC/26/27/0725", "1st Semester", "COS 242", "Data Structures", 3, 69, "B", 4),
    ("CSC/26/27/0725", "1st Semester", "STA 111", "Descriptive Statistics", 2, 45, "D", 2),
    ("CSC/26/27/0725", "1st Semester", "MTH 101", "Elementary Mathematics", 3, 35, "F", 0),

    #Oscar Benjamin
    ("MLS/24/25/0831", "1st Semester", "MLS 301", "Clinical Chemistry", 3, 75, "B", 4),
    ("MLS/24/25/0831", "1st Semester", "BIO 101", "Entrepreneurship Studies", 3, 90, "A", 5),
    ("MLS/24/25/0831", "1st Semester", "CHE 101", "Molecular Biology And Genetics", 3, 41, "E", 1),
    ("MLS/24/25/0831", "1st Semester", "MAT 101", "Laboratory Instruments And Techniques", 2, 52, "C", 3),
    ("MLS/24/25/0831", "1st Semester", "GST 111", "Haematology", 2, 49, "D", 2),

    #Rabiu Bola
    ("ECO/26/27/0862", "1st Semester", "ECO 101", "Principles Of Economics", 3, 80, "A", 5),
    ("ECO/26/27/0862", "1st Semester", "SOC 101", "Introduction to Sociology", 2, 70, "A", 5),
    ("ECO/26/27/0862", "1st Semester", "POL 101", "Introduction To Political Science", 3, 60, "B", 4),
    ("ECO/26/27/0862", "1st Semester", "GST 111", "Communication In English", 2, 50, "C", 3),
    ("ECO/26/27/0862", "1st Semester", "ECO 103", "Development Economics", 3, 40, "D", 2),

    #Udoh David
    ("ARC/26/27/0887", "1st Semester", "ARC 101", "Introduction To Architecture", 2, 75, "B", 4),
    ("ARC/26/27/0887", "1st Semester", "ARC 108", "Basic Design And Visual Communication I", 3, 80, "A", 5),
    ("ARC/26/27/0887", "1st Semester", "ARC 105", "Technical Drawing And Freehand Sketching", 2, 62, "B", 4),
    ("ARC/26/27/0887", "1st Semester", "ARC 109", "Architectural Design Studio I", 3, 35, "F", 0),
    ("ARC/26/27/0887", "1st Semester", "GST 111", "Communication In English", 3, 42, "E", 1),
]

# Add all course results
cursor.executemany("""
INSERT INTO results
(matric_number, semester, course_code, course_title, units, score, grade, grade_point)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
ON CONFLICT(matric_number, semester, course_code)
DO UPDATE SET
    course_title = excluded.course_title,
    units = excluded.units,
    score = excluded.score,
    grade = excluded.grade,
    grade_point = excluded.grade_point
""", results)

# Save database
connection.commit()

# Confirm record counts
cursor.execute("SELECT COUNT(*) FROM students")
print("Students:", cursor.fetchone()[0])

cursor.execute("SELECT COUNT(*) FROM results")
print("Course results:", cursor.fetchone()[0])

connection.close()

print("Database created and populated successfully!")
print("Database file: students.db")

