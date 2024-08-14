from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models import PromotionOut, PromotionCreate, PromotionUpdate
from app.api import db_manager

promotion_router = APIRouter()

@promotion_router.post("/", response_model=PromotionOut, status_code=201)
async def create_promotion(payload: PromotionCreate):
    promotion_id = await db_manager.create_promotion(payload)
    response = {"promotion_id": promotion_id, **payload.dict()}
    return response

@promotion_router.get("/", response_model=List[PromotionOut])
async def get_promotions():
    return await db_manager.get_all_promotions()

@promotion_router.get("/{promotion_id}/", response_model=PromotionOut)
async def get_promotion(promotion_id: int):
    promotion = await db_manager.get_promotion(promotion_id)
    if not promotion:
        raise HTTPException(status_code=404, detail="Promotion not found")
    return promotion

@promotion_router.put("/{promotion_id}/", response_model=PromotionOut)
async def update_promotion(promotion_id: int, payload: PromotionUpdate):
    promotion = await db_manager.get_promotion(promotion_id)
    if not promotion:
        raise HTTPException(status_code=404, detail="Promotion not found")
    return await db_manager.update_promotion(promotion_id, payload)

@promotion_router.delete("/{promotion_id}/", response_model=None, status_code=204)
async def delete_promotion(promotion_id: int):
    promotion = await db_manager.get_promotion(promotion_id)
    if not promotion:
        raise HTTPException(status_code=404, detail="Promotion not found")
    await db_manager.delete_promotion(promotion_id)
    return {"detail": "Promotion deleted successfully"}
