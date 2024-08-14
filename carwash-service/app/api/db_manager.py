from pydantic import BaseModel
from typing import Optional
from datetime import datetime

from app.api.models import (
    CustomerCreate, CustomerOut, CustomerUpdate,
    VehicleCreate, VehicleOut, VehicleUpdate,
    ServiceCreate, ServiceOut, ServiceUpdate,
    TransactionCreate, TransactionOut, TransactionUpdate,
    EmployeeCreate, EmployeeOut, EmployeeUpdate,
    ShiftCreate, ShiftOut, ShiftUpdate,
    PromotionCreate, PromotionOut, PromotionUpdate,
    MembershipCreate, MembershipOut, MembershipUpdate
)

from app.api.db import (
    customer, vehicle, service, transaction, employee, shift, promotion, membership,
    database
)

# Customer functions
async def create_customer(payload: CustomerCreate):
    query = customer.insert().values(**payload.dict())
    return await database.execute(query=query)

async def get_all_customers():
    query = customer.select()
    results = await database.fetch_all(query=query)
    return [CustomerOut(**result) for result in results]

async def get_customer(id: int):
    query = customer.select().where(customer.c.customer_id == id)
    result = await database.fetch_one(query=query)
    return CustomerOut(**result) if result else None

async def delete_customer(id: int):
    query = customer.delete().where(customer.c.customer_id == id)
    return await database.execute(query=query)

async def update_customer(id: int, payload: CustomerUpdate):
    query = customer.update().where(customer.c.customer_id == id).values(**payload.dict())
    await database.execute(query=query)
    return await get_customer(id)

# Vehicle functions
async def create_vehicle(payload: VehicleCreate):
    query = vehicle.insert().values(**payload.dict())
    return await database.execute(query=query)

async def get_all_vehicles():
    query = vehicle.select()
    results = await database.fetch_all(query=query)
    return [VehicleOut(**result) for result in results]

async def get_vehicle(id: int):
    query = vehicle.select().where(vehicle.c.vehicle_id == id)
    result = await database.fetch_one(query=query)
    return VehicleOut(**result) if result else None

async def delete_vehicle(id: int):
    query = vehicle.delete().where(vehicle.c.vehicle_id == id)
    return await database.execute(query=query)

async def update_vehicle(id: int, payload: VehicleUpdate):
    query = vehicle.update().where(vehicle.c.vehicle_id == id).values(**payload.dict())
    await database.execute(query=query)
    return await get_vehicle(id)

# Service functions
async def create_service(payload: ServiceCreate):
    query = service.insert().values(**payload.dict())
    return await database.execute(query=query)

async def get_all_services():
    query = service.select()
    results = await database.fetch_all(query=query)
    return [ServiceOut(**result) for result in results]

async def get_service(id: int):
    query = service.select().where(service.c.service_id == id)
    result = await database.fetch_one(query=query)
    return ServiceOut(**result) if result else None

async def delete_service(id: int):
    query = service.delete().where(service.c.service_id == id)
    return await database.execute(query=query)

async def update_service(id: int, payload: ServiceUpdate):
    query = service.update().where(service.c.service_id == id).values(**payload.dict())
    await database.execute(query=query)
    return await get_service(id)

# Transaction functions
async def create_transaction(payload: TransactionCreate):
    query = transaction.insert().values(**payload.dict())
    return await database.execute(query=query)

async def get_all_transactions():
    query = transaction.select()
    results = await database.fetch_all(query=query)
    return [TransactionOut(**result) for result in results]

async def get_transaction(id: int):
    query = transaction.select().where(transaction.c.transaction_id == id)
    result = await database.fetch_one(query=query)
    return TransactionOut(**result) if result else None

async def delete_transaction(id: int):
    query = transaction.delete().where(transaction.c.transaction_id == id)
    return await database.execute(query=query)

async def update_transaction(id: int, payload: TransactionUpdate):
    query = transaction.update().where(transaction.c.transaction_id == id).values(**payload.dict())
    await database.execute(query=query)
    return await get_transaction(id)

# Employee functions
async def create_employee(payload: EmployeeCreate):
    query = employee.insert().values(**payload.dict())
    return await database.execute(query=query)

async def get_all_employees():
    query = employee.select()
    results = await database.fetch_all(query=query)
    return [EmployeeOut(**result) for result in results]

async def get_employee(id: int):
    query = employee.select().where(employee.c.employee_id == id)
    result = await database.fetch_one(query=query)
    return EmployeeOut(**result) if result else None

async def delete_employee(id: int):
    query = employee.delete().where(employee.c.employee_id == id)
    return await database.execute(query=query)

async def update_employee(id: int, payload: EmployeeUpdate):
    query = employee.update().where(employee.c.employee_id == id).values(**payload.dict())
    await database.execute(query=query)
    return await get_employee(id)

# Shift functions
async def create_shift(payload: ShiftCreate):
    query = shift.insert().values(**payload.dict())
    return await database.execute(query=query)

async def get_all_shifts():
    query = shift.select()
    results = await database.fetch_all(query=query)
    return [ShiftOut(**result) for result in results]

async def get_shift(id: int):
    query = shift.select().where(shift.c.shift_id == id)
    result = await database.fetch_one(query=query)
    return ShiftOut(**result) if result else None

async def delete_shift(id: int):
    query = shift.delete().where(shift.c.shift_id == id)
    return await database.execute(query=query)

async def update_shift(id: int, payload: ShiftUpdate):
    query = shift.update().where(shift.c.shift_id == id).values(**payload.dict())
    await database.execute(query=query)
    return await get_shift(id)

# Promotion functions
async def create_promotion(payload: PromotionCreate):
    query = promotion.insert().values(**payload.dict())
    return await database.execute(query=query)

async def get_all_promotions():
    query = promotion.select()
    results = await database.fetch_all(query=query)
    return [PromotionOut(**result) for result in results]

async def get_promotion(id: int):
    query = promotion.select().where(promotion.c.promotion_id == id)
    result = await database.fetch_one(query=query)
    return PromotionOut(**result) if result else None

async def delete_promotion(id: int):
    query = promotion.delete().where(promotion.c.promotion_id == id)
    return await database.execute(query=query)

async def update_promotion(id: int, payload: PromotionUpdate):
    query = promotion.update().where(promotion.c.promotion_id == id).values(**payload.dict())
    await database.execute(query=query)
    return await get_promotion(id)

# Membership functions
async def create_membership(payload: MembershipCreate):
    query = membership.insert().values(**payload.dict())
    return await database.execute(query=query)

async def get_all_memberships():
    query = membership.select()
    results = await database.fetch_all(query=query)
    return [MembershipOut(**result) for result in results]

async def get_membership(id: int):
    query = membership.select().where(membership.c.membership_id == id)
    result = await database.fetch_one(query=query)
    return MembershipOut(**result) if result else None

async def delete_membership(id: int):
    query = membership.delete().where(membership.c.membership_id == id)
    return await database.execute(query=query)

async def update_membership(id: int, payload: MembershipUpdate):
    query = membership.update().where(membership.c.membership_id == id).values(**payload.dict())
    await database.execute(query=query)
    return await get_membership(id)
