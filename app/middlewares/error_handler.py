from __future__ import annotations
from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
import traceback

class ErrorHandlingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            response = await call_next(request)
            return response
        except Exception as ex:
            # In production you might log with Sentry etc.
            return JSONResponse(
                status_code=500,
                content={"detail": "Internal Server Error", "error": str(ex)},
            )
