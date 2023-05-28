import random
from typing import AsyncGenerator

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, joinedload, selectinload

from models import Recipe, ProductRecipe
from schemas import Product, Ration
from schemas import Recipe as RecipeSchema
from settings import DB_URI

engine = create_async_engine(DB_URI)

async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def generate_rations(calories: int, session: AsyncSession):
    stmt = select(Recipe).options(selectinload(Recipe.product).selectinload(ProductRecipe.product)).where(Recipe.calories <= calories // 3)
    res = await session.execute(stmt)
    recipes = res.scalars().all()
    diet = {
        'monday': [],
        'tuesday': [],
        'wednesday': [],
        'thursday': [],
        'friday': [],
        'saturday': [],
        'sunday': []
    }

    for day in diet:
        remaining_calories = calories
        for _ in range(3):  # минимум 3 блюда
            suitable_recipes = [recipe for recipe in recipes if recipe.calories <= remaining_calories and recipe.name not in [i.name for i in diet[day]]]
            if not suitable_recipes:  # нет подходящих рецептов, выходим из цикла
                break
            chosen_recipe = random.choice(suitable_recipes)  # выбираем случайное блюдо из подходящих
            products = []
            for product_recipe in chosen_recipe.product:
                products.append(Product(
                    name=product_recipe.product.name,
                    weight=product_recipe.weight
                ))
            recipe_base = RecipeSchema(
                name=chosen_recipe.name,
                calories=chosen_recipe.calories,
                img=chosen_recipe.img,
                url=chosen_recipe.url,
                weight=chosen_recipe.weight,
                products=products
            )
            diet[day].append(recipe_base)
            remaining_calories -= chosen_recipe.calories

        # Если после выбора 3 блюд остались калории, выбираем еще блюда
        while remaining_calories > min(recipe.calories for recipe in recipes):
            suitable_recipes = [recipe for recipe in recipes if recipe.calories <= remaining_calories and recipe.name not in [i.name for i in diet[day]]]
            if not suitable_recipes:  # нет подходящих рецептов, выходим из цикла
                break
            chosen_recipe = random.choice(suitable_recipes)  # выбираем случайное блюдо из подходящих
            products = []
            for product_recipe in chosen_recipe.product:
                products.append(Product(
                    name=product_recipe.product.name,
                    weight=product_recipe.weight
                ))
            recipe_base = RecipeSchema(
                name=chosen_recipe.name,
                calories=chosen_recipe.calories,
                img=chosen_recipe.img,
                url=chosen_recipe.url,
                weight=chosen_recipe.weight,
                products=products
            )
            diet[day].append(recipe_base)
            remaining_calories -= chosen_recipe.calories

    return Ration(**diet)
