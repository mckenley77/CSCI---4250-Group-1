from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, ForeignKeyConstraint
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
  pass

class User(Base):
  __tablename__="users"

  id = Column(Integer, primary_key=True, autoincrement=True)
  username = Column(String)
  password = Column(String)
  firstname = Column(String)
  lastname = Column(String)
