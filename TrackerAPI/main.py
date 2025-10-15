from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from api_models import UserModel
from db_models import Base, User
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
