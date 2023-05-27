from typing import List

from pydantic import BaseModel


class Product(BaseModel):
    name: str
    weight: float


class Recipe(BaseModel):
    name: str
    weight: float
    calories: float
    photo: str
    products: List[Product]


class Ration(BaseModel):
    monday: List[Recipe]
    tuesday: List[Recipe]
    wednesday: List[Recipe]
    thursday: List[Recipe]
    friday: List[Recipe]
    saturday: List[Recipe]
    sunday: List[Recipe]


class Ids(BaseModel):
    ids: List[str]
