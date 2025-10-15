from pydantic import BaseModel

class UserModel(BaseModel):
  username : str
  password : str
  firstname : str
  lastname : str
