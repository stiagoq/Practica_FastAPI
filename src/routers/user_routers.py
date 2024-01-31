from fastapi import FastAPI, Path, Query, APIRouter
from typing import List 
from src.models.user_models import *
from fastapi.responses import JSONResponse

user_router = APIRouter()
users : List[User] = []
list_id = []

@user_router.get('/', tags =["User"], response_model = List[User], status_code= 200)
def get_users():
    content =[user.dict() for user in users]
    return JSONResponse(content=content, status_code= 200)

@user_router.post('/', tags =["User"],  response_model = List[User], status_code= 201)
def create_user( user: CreateUser):
    user_model = User(**user.dict())
    users.append(user_model)
    list_id.append(user.id)
    content = [user.dict() for user in users]
    return JSONResponse(content=content, status_code= 201)


@user_router.put('/{id}', tags =["User"], response_model = List[User], status_code=200)
def update_user(user: UpdateUser, id :int = Path(gt=0)):
    if id in list_id:
        for item in users:
            if item.id == id:
                item.name = user.name
                item.password = user.password
                item.email = user.email
        content = [user.dict() for user in users]
        return JSONResponse(content=content, status_code=200)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "No se encuentra usuario")
    

@user_router.delete('/{id}', tags =["User"], response_model=List[User], status_code=200)
def delete_user(id:int = Path(gt=0)):
    if id in list_id:
        for user in users:
            if user.id == id:
                users.remove(user)
                list_id.remove(id)
        content = [user.dict() for user in users]
        return JSONResponse(content=content, status_code=200)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "No se encuentra usuario")
