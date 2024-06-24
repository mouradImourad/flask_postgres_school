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
    subject_id = db.Column(db.Integer, foreign_key=True)

    def to_dict(self):
        return {
            "id":self.student_id,
            "first_name":self.first_name,
            "last_name":self.last_name,
            "age":self.age
        }

class Teacher(db.Model):
    __tablename__= 'teachers'
    teacher_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.String(1))
    subject_id = db.Column(db.Integer, foreign_key=True)

    def to_dict(self):
        return {
            "teacher_id":self.teacher_id,
            "first_name":self.first_name,
            "last_name":self.last_name,
            "age":self.age,
            "subject_id":self.subject_id
        }

class Subject(db.Model):
    __tablename__= 'subjects'
    subject_id = db.Column(db.Integer, primary_key=True)
    subject_name = db.Column(db.String(50))

    def to_dict(self):
        return {
            "subject_id":self.subject_id,
            "subject_name":self.subject_name
        }

@app.route('/students', methods=['GET'])
def get_students():
    result = []
    students = Student.query.all()
    for student in students:
        result.append(student.to_dict())
    return jsonify(result)

@app.route('/teachers', methods=['GET'])
def get_teachers():
    teachers = Teacher.query.all()
    result = []
    for teacher in teachers:
        result.append(teacher.to_dict())
    return jsonify(result)

@app.route('/subjects', methods=['GET'])
def get_subjects():
    subjects = Subject.query.all()
    result = []
    for subject in subjects:
       result.append(subject.to_dict())
    return jsonify(result)

app.run(debug=True)