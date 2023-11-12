from flask import Flask, request, jsonify
import sqlite3
from flask import render_template

app = Flask(__name__)


# Endpoint to fetch student details by ID
@app.route('/get_student/<int:student_id>', methods=['GET'])
def get_student(student_id):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM students WHERE id = ?', (student_id,))
    student = cursor.fetchone()

    conn.close()

    if student:
        student_dict = {
            'id': student[0],
            'name': student[1],
            'age': student[2],
            'address': student[3],
            'major': student[4],
            'rfc': student[5]
        }
        # Render the HTML template with student data
        return render_template('student_template.html', student=student_dict)
    else:
        return jsonify({'error': 'Student not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
