from data import db
from model.school import School
from model.student import Student

db.drop_all()
db.create_all()

school1 = School('天津大学','003',2)
school2 = School('蓝翔技校','004')

student1 = Student('马师傅','040191',school1)

student2 = Student('王小帅','000000')
student2.my_school= school1 #my_school就是relationship定义的字段

student3 = Student('续师傅','3333333')
student3.my_school= school2

student4= Student('王司机','222222')
student4.my_school= school2



db.session.add(student1)
db.session.add(student2)
db.session.add(student3)
db.session.add(student4)

db.session.commit()