from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from api_models import UserModel, StudentModel, CourseModel, InstructorModel
from db_models import Base, User, Student, Course, Instructor
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


#Set up our local DB session
SQLALCHEMY_DATABASE_URL = "sqlite:///./student_tracker.db"
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
  userToLogin = session.query(User).filter(User.username == username and User.password == password).first()
  return userToLogin

@app.get("/users/")
async def GetUsersAsync():
  return session.query(User).all()

@app.post("/users/")
async def CreateUserAsync(user : UserModel):
  idNum = session.query(User).count()
  session.add(User(
    id=idNum,
    username=user.username,
    password=user.password,
    firstname=user.firstname,
    lastname=user.lastname
  ))
  session.commit()
  return "success"

#course

@app.get("/course/{id}")
async def GetCourseAsync(id : int):
  courseGet = session.query(Course).filter(Course.id == id).first()
  return courseGet

@app.get("/course/")
async def GetCoursesAsync():
  return session.query(Course).all()

@app.post("/course/")
async def CreateUserAsync(course : CourseModel):
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
