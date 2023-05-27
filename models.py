import uuid

from sqlalchemy import Column, ForeignKey, String, Float, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Recipe(Base):
    __tablename__ = "recipe"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    weight = Column(Float, nullable=False)
    calories = Column(Float, nullable=False)
    img = Column(String, nullable=False)
    url = Column(String, nullable=False)
    product = relationship("ProductRecipe", backref='recipe')


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    recipe = relationship("ProductRecipe", backref='product')


class ProductRecipe(Base):
    __tablename__ = "product_recipe"

    id = Column(Integer, primary_key=True, index=True)
    recipe_id = Column(Integer, ForeignKey("recipe.id"))
    product_id = Column(Integer, ForeignKey("product.id"))
    weight = Column(Float, nullable=False)



