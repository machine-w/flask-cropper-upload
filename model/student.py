from data import db
class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(100),nullable = False)
    stuNo = db.Column(db.String(100),nullable = False)
    age = db.Column(db.Integer,nullable=False)
    phone = db.Column(db.String(100),nullable = True)
    address = db.Column(db.String(100),nullable = True)
    gender = db.Column(db.Integer,nullable=False)
    state = db.Column(db.Integer,nullable=False)

    #外键
    school_id = db.Column(db.Integer,db.ForeignKey("school.id")) # 这里的school是表名（__tablename__）
    my_school = db.relationship("School",backref=db.backref("students")) # 这里的School是类名（class后面那个）

    def __init__(self,name,stuNo,school=None,classs= None,age=0,phone="",\
                 address="",gender=0,\
                 state=0):
        self.name = name
        self.classs = classs
        self.stuNo = stuNo
        self.age = age
        self.phone = phone
        self.address = address
        self.gender = gender
        self.state = state
        self.my_school = school
    def __str__(self):
        return '<td>%s</td><td>%s</td>' \
            % (self.name,self.state)