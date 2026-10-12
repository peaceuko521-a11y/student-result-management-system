from flask import Flask,render_template, request
import sqlite3
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    matric_number = request.form["matric_number"]

    connection = sqlite3.connect('students.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    # Get student information
    cursor.execute(
        "SELECT * FROM students WHERE matric_number = ?" ,
        (matric_number,)
   
    )
    student = cursor.fetchone()

    if student is None:
        connection.close()
        return "Student not found. Please check your matric number and try again."

    # Get the student's course results 
    cursor.execute(
        """ SELECT semester, course_code, course_title, units, score, grade, grade_point
        FROM results WHERE matric_number = ? """, (matric_number,)
    )
    results = cursor.fetchall()
    # Calculate GPA
    total_quality_points = 0
    total_units = 0

    for result in results:
        total_quality_points += result["units"] * result["grade_point"]
        total_units += result["units"]

    if total_units > 0:
            gpa = total_quality_points / total_units
    else:
        gpa = 0.0
    
    # Calculate ranking
        
    cursor.execute("""
        SELECT matric_number,
               SUM(units * grade_point) AS quality_points,
               SUM(units) AS total_units
        FROM results
        GROUP BY matric_number
    """)
       
    all_students = cursor.fetchall()
    rankings = []

    for student_result in all_students:
        student_gpa = student_result["quality_points"] / student_result["total_units"]

        rankings.append((
            student_result["matric_number"],
            student_gpa,
            student_result["quality_points"]
        ))

    rankings.sort(key=lambda x: (x[1], x[2]), reverse=True)

    rank = next(
        i + 1 for i, item in enumerate(rankings)
        if item[0] == matric_number
    )
   
    connection.close()

    return render_template(
        "result.html", student=student, results=results, gpa=gpa, rank=rank, total_students=len(rankings))


@app.route("/check-database")
def check_database():
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM students")
    student_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM results")
    result_count = cursor.fetchone()[0]

    connection.close()

    return f"Students: {student_count}, Course results: {result_count}"

if __name__ == "__main__":
    app.run(debug=True)
