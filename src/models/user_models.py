from pydantic import BaseModel, Field, validator
from typing import List
from fastapi import HTTPException, status

list_id= []
list_username = []

class User(BaseModel):
    id : int
    username: str
    password: str
    name: str
    lastname: str
    email: str

class CreateUser(BaseModel):
    id : int
    username: str = Field(min_length=5 , max_length= 15, default= "username")
    password: str = Field(min_length=8, max_length=15, default="password")
    name: str = Field(min_length=3, max_length=15, default="usuario")
    lastname: str = Field(min_length=5, max_length=15, default="lastname")
    email: str = Field(min_length=5 , max_length= 50, default="example@example.com")

    @validator("email")
    def good_emmail(cls, email:str):
            if "@" not in email or ".com" not in email:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail= "El email no contiene '@' o '.com'")
                #raise ValueError("El email no contiene '@' o '.com'") 
            else:
                return email
                
    
    @validator("id")
    def id_good(cls, id: int):
        if(id <= 0): 
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail= "El ID debe ser  mayor a 0")

            #raise ValueError("El ID debe ser mayor a 0")
        elif id in list_id:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail= "El ID debe esta repetido")
            #raise ValueError("El ID esta repetido")
        else:
            list_id.append(id)
        return id
    
    @validator("username")
    def good_username(cls, username:str):
         if username is not None:
              if username not in list_username:
                list_username.append(username)
              else:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail= "El username esta repetido")
                #raise  ValueError("Username repetido")
         return username
              

class UpdateUser(BaseModel):
    password: str = Field(min_length=8, max_length=15)
    name: str = Field(min_length=3, max_length=15)
    lastname: str = Field(min_length=5, max_length=15)
    email: str = Field(min_length=5 , max_length= 50, default="example2@example2.com")

    @validator("email")
    def good_emmail(cls, email:str):
            if "@" not in email or ".com" not in email:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail= "El email no contiene '@' o '.com'")
                #raise ValueError("El email no contiene '@' o '.com'") 
            else:
                return email
                