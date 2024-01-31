from starlette.middleware.base import BaseHTTPMiddleware, DispatchFunction, RequestResponseEndpoint
from fastapi import FastAPI, status
from fastapi.requests import Request
from fastapi.responses import Response, JSONResponse
from starlette.responses import Response
from starlette.types import ASGIApp

class HtttpErrorHandler(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI ) -> None:
        super().__init__(app)


    async def dispatch(self, request: Request, call_next) -> Response | JSONResponse:
        try:
            return await call_next(request)
        except Exception as e:
            content = f"exec: {str(e)}"
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            return JSONResponse(content=content, status_code=status_code)