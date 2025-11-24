from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from app.api import routes_predict , routes_auth
from app.middleware.LoggingMiddleware import LoggingMiddleware
from app.core.exceptions import register_exception_handlers

app=FastAPI(title="Car Price Prediction API")

app.add_middleware(LoggingMiddleware)

app.include_router(routes_auth.router, tags=['Authentication'])
app.include_router(routes_predict.router, tags=['Prediction'])

register_exception_handlers(app)

Instrumentator().instrument(app).expose(app)

register_exception_handlers(app)

