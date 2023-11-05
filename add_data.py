import sqlite3

def add_student(name, age, address, major, rfc):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO students (name, age, address, major, rfc)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, age, address, major, rfc))

    conn.commit()
    conn.close()

# Adding sample data
add_student('John Doe', 22, '123 Main St', 'Computer Science', 'ABCD123456')
add_student('Jane Smith', 20, '456 Oak St', 'Biology', 'EFGH789012')
add_student('Bob Johnson', 25, '789 Pine St', 'Mathematics', 'IJKL345678')
