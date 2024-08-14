from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models import ServiceOut, ServiceCreate, ServiceUpdate
from app.api import db_manager

service_router = APIRouter()

@service_router.post("/", response_model=ServiceOut, status_code=201)
async def create_service(payload: ServiceCreate):
    service_id = await db_manager.create_service(payload)
    response = {"service_id": service_id, **payload.dict()}
    return response

@service_router.get("/", response_model=List[ServiceOut])
async def get_services():
    return await db_manager.get_all_services()

@service_router.get("/{service_id}/", response_model=ServiceOut)
async def get_service(service_id: int):
    service = await db_manager.get_service(service_id)
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")
    return service

@service_router.put("/{service_id}/", response_model=ServiceOut)
async def update_service(service_id: int, payload: ServiceUpdate):
    service = await db_manager.get_service(service_id)
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")
    return await db_manager.update_service(service_id, payload)

@service_router.delete("/{service_id}/", response_model=None, status_code=204)
async def delete_service(service_id: int):
    service = await db_manager.get_service(service_id)
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")
    await db_manager.delete_service(service_id)
    return {"detail": "Service deleted successfully"}
