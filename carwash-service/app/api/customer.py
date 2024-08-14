from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models import CustomerOut, CustomerCreate, CustomerUpdate
from app.api import db_manager

customer_router = APIRouter()

@customer_router.post("/", response_model=CustomerOut, status_code=201)
async def create_customer(payload: CustomerCreate):
    customer_id = await db_manager.create_customer(payload)
    response = {"customer_id": customer_id, **payload.dict()}
    return response

@customer_router.get("/", response_model=List[CustomerOut])
async def get_customers():
    return await db_manager.get_all_customers()

@customer_router.get("/{customer_id}/", response_model=CustomerOut)
async def get_customer(customer_id: int):
    customer = await db_manager.get_customer(customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@customer_router.put("/{customer_id}/", response_model=CustomerOut)
async def update_customer(customer_id: int, payload: CustomerUpdate):
    customer = await db_manager.get_customer(customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return await db_manager.update_customer(customer_id, payload)

@customer_router.delete("/{customer_id}/", response_model=None, status_code=204)
async def delete_customer(customer_id: int):
    customer = await db_manager.get_customer(customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    await db_manager.delete_customer(customer_id)
    return {"detail": "Customer deleted successfully"}
