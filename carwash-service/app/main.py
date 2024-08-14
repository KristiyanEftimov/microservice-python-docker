from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from sqlalchemy.exc import SQLAlchemyError

from app.api.db import metadata, database, engine
from app.api.customer import customer_router
from app.api.employee import employee_router
from app.api.membership import membership_router
from app.api.promotion import promotion_router
from app.api.service import service_router
from app.api.shift import shift_router
from app.api.transaction import transaction_router
from app.api.vehicle import vehicle_router

metadata.create_all(engine)

app = FastAPI(openapi_url="/api/v1/carwash/openapi.json",
              docs_url="/api/v1/carwash/docs")


@app.exception_handler(SQLAlchemyError)
async def sqlalchemy_exception_handler(request: Request, exc: SQLAlchemyError):
    return JSONResponse(
        status_code=500,
        content={
            "message": "An error occurred with the database operation", "detail": str(exc)}
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors(), "body": exc.body},
    )


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )


@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": "An internal server error occurred.",
                 "detail": str(exc)},
    )


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(customer_router, prefix='/api/v1/customer',
                   tags=['customer'])
app.include_router(employee_router, prefix='/api/v1/employee',
                   tags=['employee'])
app.include_router(membership_router, prefix='/api/v1/membership',
                   tags=['membership'])
app.include_router(promotion_router, prefix='/api/v1/promotion',
                   tags=['promotion'])
app.include_router(service_router, prefix='/api/v1/service',
                   tags=['service'])
app.include_router(shift_router, prefix='/api/v1/shift',
                   tags=['shift'])
app.include_router(transaction_router, prefix='/api/v1/transaction',
                   tags=['transaction'])
app.include_router(vehicle_router, prefix='/api/v1/vehicle',
                   tags=['vehicle'])

