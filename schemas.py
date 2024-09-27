from typing import Optional
from pydantic import BaseModel, Field

class Product(BaseModel):
    name: str
    price: float
    quantity: int
    description: Optional[str] = Field(default=None)

class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    quantity: int
    description: Optional[str]
    class Config:
        form_attribute = True

class ProductsResponse(BaseModel):
    data: list[ProductResponse]

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[int] = None
    description: Optional[str] = None
    class Config:
        from_attributes = True

