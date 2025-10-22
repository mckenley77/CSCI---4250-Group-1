from pydantic import BaseModel
from datetime import datetime, date
from typing import List, Optional

class UserModel(BaseModel):
  user_type : str
  username : str
  password : str
  firstname : str
  lastname : str
  
  
class CourseModel(BaseModel):
  courseid : int
  coursename : str
  coursecode : str
  coursedescription : str
  startdate : date
  enddate : date
  
class InstructorModel(UserModel):
  instructorid : int
  department : str
  taughtcourses : List[CourseModel]

class StudentModel(UserModel):
  studentid  : int
  major : str
  enrollmentdate : date
  locationsharingenabled : bool
  enrolledcourses : List[CourseModel]
  