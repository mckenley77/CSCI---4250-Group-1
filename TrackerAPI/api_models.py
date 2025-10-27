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
  
class MessageModel(BaseModel):
  messageid : int
  senderid : int
  recipienttype : str
  messagecontent : str
  sentat: datetime
  isread : bool
  
class BroadcastModel(BaseModel):
  broadcastid : str
  instructorid : str
  courseid : str
  message : str
  sentat : date
  recipientcount : int

class NotificationModel(BaseModel):
  notificationid : int
  userid : int
  type : str
  title : str
  message : str
  isread : bool
  createdat : datetime

class LocationModel(BaseModel):
  locationid : int
  userid : int
  latitude : float
  longitude : float
  address : str
  timestamp : datetime
  accuracy : float