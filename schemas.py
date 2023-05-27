from typing import List

from pydantic import BaseModel


class Product(BaseModel):
    name: str
    weight: float

    class Config:
        orm_mode = True


class Recipe(BaseModel):
    name: str
    calories: float
    img: str
    url: str
    weight: float
    products: List[Product]

    class Config:
        orm_mode = True


class Ration(BaseModel):
    monday: List[Recipe]
    tuesday: List[Recipe]
    wednesday: List[Recipe]
    thursday: List[Recipe]
    friday: List[Recipe]
    saturday: List[Recipe]
    sunday: List[Recipe]

    class Config:
        orm_mode = True
