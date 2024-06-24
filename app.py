from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://mourad@localhost/school'

db = SQLAlchemy(app)

class Student(db.Model):
    __tablename__= 'students'
    student_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.String(1))
    subject_id = db.Column(db.String(1))

    def to_dict(self):
        return {
            "student_id":self.student_id,
            "first_name":self.first_name,
            "last_name":self.last_name,
            "age":self.age,
            "subject_id":self.subject_id
        }

# class Teacher(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.Integer, primary_key=True)
#     last_name = db.Column(db.String(50))
#     age = db.Column(db.String(1))
#     subject = db.Column(db.String(1))

# class Subject(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     subject = db.Column(db.String(50))

@app.route('/students', methods=['GET'])
def get_students():
    result = []
    students = Student.query.all()
    for student in students:
        result.append(student.to_dict())
    return jsonify(result)

# @app.route('/teachers', methods=['GET'])
# def get_teachers():
#     teachers = Teacher.query.all()
#     result = []
#     for teacher in teachers:
#         teacher_dict ={
#             'id': teacher.id, 
#             'first_name': teacher.first_name, 
#             'last_name': teacher.last_name, 
#             'age': teacher.age, 
#             'subject': teacher.subject
#         }
#         result.append(teacher_dict)
#     print(result)
#     return jsonify(result)
# @app.route('/subjects', methods=['GET'])
# def get_subjects():
#     subjects = Subject.query.all()
#     result = []
#     for subject in subjects:
#         subject_dict ={
#             'id': subject.id,
#             'subject': subject.subject
#         }
#         result.append(subject_dict)
#     print(result)
#     return jsonify(result)

app.run(debug=True)