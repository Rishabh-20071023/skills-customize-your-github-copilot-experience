from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: str
    price: float

class ItemCreate(BaseModel):
    name: str
    description: str
    price: float

items = [
    Item(id=1, name="Notebook", description="A place to write notes.", price=5.99),
    Item(id=2, name="Pen", description="A blue ink pen.", price=1.49),
]

@app.get("/items", response_model=List[Item])
def list_items():
    return items

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/items", response_model=Item)
def create_item(item: ItemCreate):
    new_id = max([existing.id for existing in items], default=0) + 1
    new_item = Item(id=new_id, **item.dict())
    items.append(new_item)
    return new_item

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: ItemCreate):
    for index, existing in enumerate(items):
        if existing.id == item_id:
            updated_item = Item(id=item_id, **item.dict())
            items[index] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for index, existing in enumerate(items):
        if existing.id == item_id:
            items.pop(index)
            return {"detail": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")

# Run this app with: uvicorn starter-code:app --reload
