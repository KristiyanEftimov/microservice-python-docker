from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models import MembershipOut, MembershipCreate, MembershipUpdate
from app.api import db_manager

membership_router = APIRouter()

@membership_router.post("/", response_model=MembershipOut, status_code=201)
async def create_membership(payload: MembershipCreate):
    membership_id = await db_manager.create_membership(payload)
    response = {"membership_id": membership_id, **payload.dict()}
    return response

@membership_router.get("/", response_model=List[MembershipOut])
async def get_memberships():
    return await db_manager.get_all_memberships()

@membership_router.get("/{membership_id}/", response_model=MembershipOut)
async def get_membership(membership_id: int):
    membership = await db_manager.get_membership(membership_id)
    if not membership:
        raise HTTPException(status_code=404, detail="Membership not found")
    return membership

@membership_router.put("/{membership_id}/", response_model=MembershipOut)
async def update_membership(membership_id: int, payload: MembershipUpdate):
    membership = await db_manager.get_membership(membership_id)
    if not membership:
        raise HTTPException(status_code=404, detail="Membership not found")
    return await db_manager.update_membership(membership_id, payload)

@membership_router.delete("/{membership_id}/", response_model=None, status_code=204)
async def delete_membership(membership_id: int):
    membership = await db_manager.get_membership(membership_id)
    if not membership:
        raise HTTPException(status_code=404, detail="Membership not found")
    await db_manager.delete_membership(membership_id)
    return {"detail": "Membership deleted successfully"}
