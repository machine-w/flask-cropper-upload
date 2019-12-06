from data import db
from sqlalchemy.dialects.postgresql import ARRAY
class School(db.Model):
    __tablename__ = 'school'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(100),nullable = False)
    schoolNo = db.Column(db.String(30),nullable=False,unique= True)
    photos = db.Column(ARRAY(db.String(80)))
    state = db.Column(db.Integer,nullable=False)

    def __init__(self,name,schoolNo,state=1):
        self.name = name
        self.schoolNo = schoolNo
        self.photos= []
        self.state = state
    def __str__(self):
        return str((self.id,self.name,self.photos))
