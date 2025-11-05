from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from api_models import UserModel, StudentModel, CourseModel, InstructorModel, MessageModel, BroadcastModel, NotificationModel, LocationModel
from db_models import Base, User, Student, Course, Instructor, Message, Broadcast, Notification, Location, InstructorCourse, StudentCourse
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

#functions to help
def updateInTable(table, id : int, modelAttributes, data):
  session.query(table).filter(table.id == id).update({modelAttributes : data})

#API endpoints below

#users, in progress

@app.get("/users/{username}/{password}")
async def GetUserAsync(username : str, password : str):
  userToLogin = session.query(User).filter(User.username == username and User.password == password).all()
  return userToLogin

@app.get("/users/{userId}")
async def GetUserById(userId : int):
  userToLog = session.query(User).filter(User.id == userId).first()
  return userToLog

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

@app.delete('/users/{userId}')
async def DeleteUserAsync(userId : int):
  session.query(User).filter(User.id == userId).delete()
  session.commit()
  return "successfully deleted user"

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
    enrollmentdate=student.enrollmentdate
    ))
  session.commit()
  return "success"

@app.put("/students/{id}")
async def UpdateStudentAsync(studentId: int, student: StudentModel):
  studentAttributes = [student.id, student.username, student.password, student.firstname, student.lastname, student.major, student.enrollmentdate]
  modelAttributes = [Student.id, Student.username, Student.password, Student.firstname, Student.lastname, Student.major, Student.enrollmentdate]
  for i in range(7):
    updateInTable(Student, studentId, modelAttributes[i], studentAttributes[i])
  session.commit()
  return "Instructor updated successfully."

@app.get("/students/courses/{id}")
async def GetStudentCourses(id : int):
  student = session.query(Student).filter(Student.id == id).first()
  return student.enrolledcourses
  
@app.post("/students/courses/")
async def AddStudentEnrollmnt(studentId : int, courseId: int):
  session.add(StudentCourse(
    student_id=studentId,
    course_id=courseId
  ))
  session.commit()
  return "success"

@app.delete('/students/{id}')
async def DeleteStudentAsync(id : int):
  session.query(Student).filter(Student.id == id).delete()
  session.commit()
  return "successfully deleted student"

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
    department=instructor.department
    ))
  session.commit()
  return "success"

@app.put("/instructors/{id}")
async def UpdateInstructorAsync(instructorId: int, instructor: InstructorModel):
  instructorAttributes = [instructor.instructorid, instructor.username, instructor.password, instructor.firstname, instructor.lastname, instructor.department]
  modelAttributes = [Instructor.instructorid, Instructor.username, Instructor.password, Instructor.firstname, Instructor.lastname, Instructor.department]
  for i in range(6):
    updateInTable(Instructor, instructorId, modelAttributes[i], instructorAttributes[i])
  session.commit()
  return "Instructor updated successfully."

@app.get("/instructors/courses/{id}")
async def GetInstructorCourses(id : int):
  instructor = session.query(Instructor).filter(Instructor.id == id).first()
  return instructor.taughtcourses
  
@app.post("/instructors/courses/")
async def AddCourseInstructor(instructorId : int, courseId: int):
  session.add(InstructorCourse(
    instructor_id=instructorId,
    course_id=courseId
  ))
  session.commit()
  return "success"
  
@app.delete('/instructors/{id}')
async def DeleteInstructorAsync(id : int):
  session.query(Instructor).filter(Instructor.id == id).delete()
  session.commit()
  return "successfully deleted instructor"


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

@app.put("/course/{id}")
async def UpdateCourseAsync(courseId: int, course: CourseModel):
  courseAttributes = [course.id, course.coursename, course.coursecode, course.coursedescription, course.startdate, course.enddate]
  modelAttributes = [Course.id, Course.coursename, Course.coursecode, Course.coursedescription, Course.startdate, Course.enddate]
  for i in range(6):
    updateInTable(Course, courseId, modelAttributes[i], courseAttributes[i])
  session.commit()
  return "Course updated successfully."

@app.delete('/course/{id}')
async def DeleteCourseAsync(id : int):
  session.query(Course).filter(Course.id == id).delete()
  session.commit()
  return "successfully deleted course"


#Message 

@app.get("/messages/{id}")
async def GetMessageAsync(id: int):
  messageGet = session.query(Message).filter(Message.id == id).first()
  return messageGet

@app.get("/messages/")
async def GetMessagesAsync():
  return session.query(Message).all()

@app.get("/messages/{senderid}/{recipientid}")
async def GetMessagesToUserAsync(senderid: int, recipientid: int):
  messages = session.query(Message).filter(Message.senderid == senderid and Message.recipientid == recipientid).order_by(Message.sentat).all()
  return messages

@app.get("/messages/user/{userId}")
async def GetMessagesByUserAsync(userId: int):
  messages = session.query(Message).filter(Message.senderid == userId or Message.recipientid == userId).order_by(Message.sentat).all()
  return messages

@app.post("/messages/")
async def PostMessageAsync(message : MessageModel):
  idNum = session.query(Message).count()
  session.add(Message(
    id=idNum,
    senderid = message.senderid,
    recipientid = message.recipientid,
    recipienttype = message.recipienttype,
    messagecontent = message.messagecontent,
    sentat = message.sentat,
    isread = message.isread
  ))
  session.commit()
  return "success"

@app.put("/messages/{id}")
async def UpdateMessagesAsync(msgId: int, message: MessageModel):
  messageAttributes = [message.id, message.senderid, message.recipientid, message.recipienttype, message.messagecontent, message.sentat, message.isread]
  modelAttributes = [Message.id, Message.senderid, Message.recipientid, Message.recipienttype, Message.messagecontent, Message.sentat, Message.isread]
  for i in range(6):
    updateInTable(Message, msgId, modelAttributes[i], messageAttributes[i])
  session.commit()
  return "Course updated successfully."

@app.delete('/messages/{id}')
async def DeleteMessageAsync(id : int):
  session.query(Message).filter(Message.id == id).delete()
  session.commit()
  return "successfully deleted message"


#Broadcast

@app.get("/broadcast/{id}")
async def GetBroadcastAsync(id: int):
  broadcastGet = session.query(Broadcast).filter(Broadcast.id == id).first()
  return broadcastGet

@app.get("/broadcast/")
async def GetBroadcastsAsync():
  return session.query(Broadcast).all()

@app.get("/broadcast/{courseId}")
async def GetBroadcastByClassAsync(courseId : int):
  courseMessages = session.query(Broadcast).filter(Broadcast.courseid == id).all()
  return courseMessages

@app.post("/broadcast/")
async def CreateBroadcastAsync(broadcast : BroadcastModel):
  session.add(Broadcast(
    instuctorid = broadcast.instructorid,
    courseid = broadcast.courseid,
    message = broadcast.message,
    sentat = broadcast.senat,
    recipientcount = broadcast.recipientcount
  ))
  session.commit()
  return "success"

@app.delete('/broadcast/{id}')
async def DeleteBroadcastAsync(id : int):
  session.query(Broadcast).filter(Broadcast.id == id).delete()
  session.commit()
  return "successfully deleted user"


#Notification
@app.get("/notification/{id}")
async def GetNotificationAsync(id: int):
  notificationGet = session.query(Notification).filter(Notification.id == id).first()
  return notificationGet

@app.get("/notifications/")
async def GetNotificationsAsync():
  return session.query(Notification).all()

@app.post("/notifications/")
async def PostNotificationAsync(notification : NotificationModel):
  idNum = session.query(Notification).count()
  session.add(Notification(
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

@app.delete('/notifications/{id}')
async def DeleteNotificationAsync(id : int):
  session.query(Notification).filter(Notification.id == id).delete()
  session.commit()
  return "successfully deleted notification"

#Location

@app.get("/location/{id}/{userid}")
async def GetLocataionAsync(id: int, userid: int):
  locationGet = session.Query(Location).filter(Location.id == id and Location.userid == userid)
  return locationGet

@app.get("/location/")
async def GetLocationsAsync():
  return session.query(Location).all()

@app.post("/location/")
async def PostLocationAsync(location : LocationModel):
  idNum  = session.query(Location).count()
  session.add(Location(
    id=idNum,
    userid=location.userid,
    latitude=location.latitude,
    longitude=location.longitude,
    address=location.address,
    timestamp=location.timestamp,
    accuracy=location.accuracy
  ))
  session.commit()
  return "success"


@app.delete('/location/{id}')
async def DeleteLocationAsync(id : int):
  session.query(Location).filter(Location.id == id).delete()
  session.commit()
  return "successfully deleted location"