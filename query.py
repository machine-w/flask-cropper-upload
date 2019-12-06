from data import db
from model.school import School
from model.student import Student

alls = School.query.all()

for school in alls:
    print('学校：------------------------------------')
    print('<',school.name,school.state,school.id,school.schoolNo,'>')
    print('学生们：')
    for student in school.students: #这里的students就是，relationship定义的时候 backref中定义的
        print('     ',student.name)
    print('------------------------------------------')

