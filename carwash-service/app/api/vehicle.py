from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models import VehicleOut, VehicleCreate, VehicleUpdate
from app.api import db_manager

vehicle_router = APIRouter()

@vehicle_router.post("/", response_model=VehicleOut, status_code=201)
async def create_vehicle(payload: VehicleCreate):
    vehicle_id = await db_manager.create_vehicle(payload)
    response = {"vehicle_id": vehicle_id, **payload.dict()}
    return response

@vehicle_router.get("/", response_model=List[VehicleOut])
async def get_vehicles():
    return await db_manager.get_all_vehicles()

@vehicle_router.get("/{vehicle_id}/", response_model=VehicleOut)
async def get_vehicle(vehicle_id: int):
    vehicle = await db_manager.get_vehicle(vehicle_id)
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return vehicle

@vehicle_router.put("/{vehicle_id}/", response_model=VehicleOut)
async def update_vehicle(vehicle_id: int, payload: VehicleUpdate):
    vehicle = await db_manager.get_vehicle(vehicle_id)
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return await db_manager.update_vehicle(vehicle_id, payload)

@vehicle_router.delete("/{vehicle_id}/", response_model=None, status_code=204)
async def delete_vehicle(vehicle_id: int):
    vehicle = await db_manager.get_vehicle(vehicle_id)
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    await db_manager.delete_vehicle(vehicle_id)
    return {"detail": "Vehicle deleted successfully"}
