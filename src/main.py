from fastapi import FastAPI
from src.routers.user_routers import *
from src.utils.http_error_handler import *

app = FastAPI()

app.include_router(prefix="/user", router=user_router)
app.middleware(HtttpErrorHandler)

