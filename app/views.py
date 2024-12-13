from fastapi import APIRouter
from app.models import Item
from fastapi import HTTPException

router = APIRouter()

# In-memory database for simplicity
db = []

@router.post("/items/")
async def create_item(item: Item):
    db.append(item)
    return { "item": item}

@router.get("/items/")
async def get_items():
    return db


@router.delete("/items/{item_id}")
async def delete_item(item_id: int):
   return {"message": "Item deleted", "item":delete_item}

@router.put("/items/{item_id}")
async def update_item(item_id: int, updated_item: Item):
    return {"message": "Item updated", "item": updated_item}

