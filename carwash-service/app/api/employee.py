from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models import EmployeeOut, EmployeeCreate, EmployeeUpdate
from app.api import db_manager

employee_router = APIRouter()

@employee_router.post("/", response_model=EmployeeOut, status_code=201)
async def create_employee(payload: EmployeeCreate):
    employee_id = await db_manager.create_employee(payload)
    response = {"employee_id": employee_id, **payload.dict()}
    return response

@employee_router.get("/", response_model=List[EmployeeOut])
async def get_employees():
    return await db_manager.get_all_employees()

@employee_router.get("/{employee_id}/", response_model=EmployeeOut)
async def get_employee(employee_id: int):
    employee = await db_manager.get_employee(employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

@employee_router.put("/{employee_id}/", response_model=EmployeeOut)
async def update_employee(employee_id: int, payload: EmployeeUpdate):
    employee = await db_manager.get_employee(employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return await db_manager.update_employee(employee_id, payload)

@employee_router.delete("/{employee_id}/", response_model=None, status_code=204)
async def delete_employee(employee_id: int):
    employee = await db_manager.get_employee(employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    await db_manager.delete_employee(employee_id)
    return {"detail": "Employee deleted successfully"}
