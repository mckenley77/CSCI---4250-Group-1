from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, ForeignKeyConstraint, Date, DateTime, Table
from typing import List
from sqlalchemy.orm import DeclarativeBase, relationship, Mapped, mapped_column

class Base(DeclarativeBase):
  pass

class User(Base):
  __tablename__="user"

  id = Column(Integer, primary_key=True, autoincrement=True)
  user_type = Column(String(32), nullable=False)
  username = Column(String)
  password = Column(String)
  firstname = Column(String)
  lastname = Column(String)
  __mapper_args__ = {'polymorphic_on': user_type}
  
class StudentCourse(Base):
  __tablename__="student_course_assn"
  student_id: Mapped[int] = mapped_column(ForeignKey("student.id"), primary_key=True)
  course_id: Mapped[int] = mapped_column(ForeignKey("course.id"), primary_key=True)
  course: Mapped["Course"] = relationship()
  
class InstructorCourse(Base):
  __tablename__="instructor_course_assn"
  instructor_id: Mapped[int] = mapped_column(ForeignKey("instructor.id"), primary_key=True)
  course_id: Mapped[int] = mapped_column(ForeignKey("course.id"), primary_key=True)
  course: Mapped["Course"] = relationship()

class Course(Base):
  __tablename__="course"
  id = Column(Integer, primary_key=True, autoincrement=True)
  coursename = Column(String, nullable=False)
  coursecode = Column(String, nullable=False)
  coursedescription = Column(String(200))
  startdate = Column(Date)
  enddate = Column(Date)
  
class Student(User):
  __tablename__="student"
  __mapper_args__ = {'polymorphic_identity': 'student'}
  id: Mapped[int] = mapped_column(ForeignKey("user.id"), primary_key=True, autoincrement=True, use_existing_column=True)
  major = Column(String)
  enrollmentdate = Column(Date)
  locationsharingenabled = Column(Boolean)
  enrolledcourses: Mapped[List[StudentCourse]] = relationship()
  

class Instructor(User):
  __tablename__="instructor"
  __mapper_args__ = {'polymorphic_identity': 'instructor'}
  id: Mapped[int] = mapped_column(ForeignKey("user.id"), primary_key=True, autoincrement=True, use_existing_column=True)
  department = Column(String)
  taughtcourses: Mapped[List[InstructorCourse]] = relationship()



