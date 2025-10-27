from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from api_models import UserModel, StudentModel, CourseModel, InstructorModel, MessageModel, BroadcastModel, NotificationModel, LocationModel
from db_models import Base, User, Student, Course, Instructor, Message, Broadcast, Notification, Location
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


#Set up our local DB session
SQLALCHEMY_DATABASE_URL = "sqlite:///././student_tracker.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

#This binds our ORM class model
Base.metadata.create_all(bind=engine)

#Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# to run: uvicorn main:app --reload
app = FastAPI()

#API endpoints below

#users, in progress

@app.get("/users/{username}/{password}")
async def GetUserAsync(username : str, password : str):
  userToLogin = session.query(User).filter(User.username == username and User.password == password).all()
  return userToLogin

@app.get("/users/")
async def GetUsersAsync():
  return session.query(User).all()

@app.post("/users/")
async def CreateUserAsync(user : UserModel):
  idNum = session.query(User).count()
  session.add(User(
    id=idNum,
    user_type = user.user_type,
    username=user.username,
    password=user.password,
    firstname=user.firstname,
    lastname=user.lastname
  ))
  session.commit()
  return "success"

#student
@app.get("/students/{id}")
async def GetStudentAsync(id : int):
  studentToGet = session.query(Student).filter(Student.id == id).first()
  return studentToGet

@app.get("/students/")
async def GetStudentsAsync():
  return session.query(Student).all()

@app.post("/students/")
async def CreateStudentAsync(student : StudentModel):
  idNum = session.query(Student).count()
  session.add(Student(
    id=idNum,
    username=student.username,
    password=student.password,
    firstname=student.firstname,
    lastname=student.lastname,
    major=student.major,
    enrollmentdate=student.enrollmentdate,
    locationsharingenabled=student.locationsharingenabled,
    enrollecourses=student.enrolledcourses
    ))
  session.commit()
  return "success"

#instructor
@app.get("/instructors/{id}")
async def GetInstructorAsync(id : int):
  instructorToGet = session.query(Instructor).filter(Instructor.id == id).first()
  return instructorToGet

@app.get("/instructors/")
async def GetInstructorsAsync():
  return session.query(Instructor).all()

@app.post("/instructors/")
async def CreateInstructorAsync(instructor : InstructorModel):
  idNum = session.query(Student).count()
  session.add(Student(
    id=idNum,
    username=instructor.username,
    password=instructor.password,
    firstname=instructor.firstname,
    lastname=instructor.lastname,
    department=instructor.department,
    taughtcourses=instructor.taughtcourses
    ))
  session.commit()
  return "success"

#course, in progress
@app.get("/course/{id}")
async def GetCourseAsync(id : int):
  courseGet = session.query(Course).filter(Course.id == id).first()
  return courseGet

@app.get("/course/")
async def GetCoursesAsync():
  return session.query(Course).all()

@app.post("/course/")
async def CreateCourseAsync(course : CourseModel):
  idNum = session.query(Course).count()
  session.add(Course(
    id=idNum,
    coursename = course.coursename,
    coursecode = course.coursecode,
    coursedescription = course.coursedescription,
    startdate = course.startdate,
    enddate = course.enddate
  ))
  session.commit()
  return "success"

#Message / Broadcast

@app.get("/messages/{id}")
async def GetMessageAsync(id: int):
  messageGet = session.query(Message).filter(Message.id == id).first()
  return messageGet

@app.get("/messages/")
async def GetMessagesAsync():
  return session.query(Message).all()

@app.post("/messages/")
async def PostMessageAsync(message : MessageModel):
  idNum = session.query(Message).count()
  session.add(Message(
    id=idNum,
    senderid = message.senderid,
    recipienttype = message.recipienttype,
    messagecontent = message.messagecontent,
    sentat = message.sentat,
    isread = message.isread
  ))
  session.commit()
  return "success"



#Notification
@app.get("/notification/{id}")
async def GetNotificationAsync(id: int):
  notificationGet = session.query(Notification).filter(Notification.id == id).first()
  return notificationGet

@app.get("/notifications/")
async def GetnotificationsAsync():
  return session.query(Notification).all()

@app.post("/notifications/")
async def PostnotificationAsync(notification : NotificationModel):
  idNum = session.query(Notification).count()
  session.add(notification(
    id=idNum,
    userid = notification.userid,
    type = notification.type,
    title = notification.title,
    message = notification.message,
    isread = notification.isread,
    createdat = notification.createdat
  ))
  session.commit()
  return "success"

