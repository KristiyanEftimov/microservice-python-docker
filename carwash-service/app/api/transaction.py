from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models import TransactionOut, TransactionCreate, TransactionUpdate
from app.api import db_manager

transaction_router = APIRouter()

@transaction_router.post("/", response_model=TransactionOut, status_code=201)
async def create_transaction(payload: TransactionCreate):
    transaction_id = await db_manager.create_transaction(payload)
    response = {"transaction_id": transaction_id, **payload.dict()}
    return response

@transaction_router.get("/", response_model=List[TransactionOut])
async def get_transactions():
    return await db_manager.get_all_transactions()

@transaction_router.get("/{transaction_id}/", response_model=TransactionOut)
async def get_transaction(transaction_id: int):
    transaction = await db_manager.get_transaction(transaction_id)
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction

@transaction_router.put("/{transaction_id}/", response_model=TransactionOut)
async def update_transaction(transaction_id: int, payload: TransactionUpdate):
    transaction = await db_manager.get_transaction(transaction_id)
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return await db_manager.update_transaction(transaction_id, payload)

@transaction_router.delete("/{transaction_id}/", response_model=None, status_code=204)
async def delete_transaction(transaction_id: int):
    transaction = await db_manager.get_transaction(transaction_id)
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    await db_manager.delete_transaction(transaction_id)
    return {"detail": "Transaction deleted successfully"}
