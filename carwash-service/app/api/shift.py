from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models import ShiftOut, ShiftCreate, ShiftUpdate
from app.api import db_manager

shift_router = APIRouter()

@shift_router.post("/", response_model=ShiftOut, status_code=201)
async def create_shift(payload: ShiftCreate):
    shift_id = await db_manager.create_shift(payload)
    response = {"shift_id": shift_id, **payload.dict()}
    return response

@shift_router.get("/", response_model=List[ShiftOut])
async def get_shifts():
    return await db_manager.get_all_shifts()

@shift_router.get("/{shift_id}/", response_model=ShiftOut)
async def get_shift(shift_id: int):
    shift = await db_manager.get_shift(shift_id)
    if not shift:
        raise HTTPException(status_code=404, detail="Shift not found")
    return shift

@shift_router.put("/{shift_id}/", response_model=ShiftOut)
async def update_shift(shift_id: int, payload: ShiftUpdate):
    shift = await db_manager.get_shift(shift_id)
    if not shift:
        raise HTTPException(status_code=404, detail="Shift not found")
    return await db_manager.update_shift(shift_id, payload)

@shift_router.delete("/{shift_id}/", response_model=None, status_code=204)
async def delete_shift(shift_id: int):
    shift = await db_manager.get_shift(shift_id)
    if not shift:
        raise HTTPException(status_code=404, detail="Shift not found")
    await db_manager.delete_shift(shift_id)
    return {"detail": "Shift deleted successfully"}
