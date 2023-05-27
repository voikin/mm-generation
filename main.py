import random
from typing import Dict, List

from bson import ObjectId
from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from motor.motor_asyncio import AsyncIOMotorClient
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import Recipe, Product
from schemas import Ration
from settings import mongo_uri
from utils import get_async_session, generate_rations

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    app.state.mongodb_client = AsyncIOMotorClient(mongo_uri)
    app.state.mongodb = app.state.mongodb_client["generator"]


@app.on_event("shutdown")
async def shutdown_event():
    app.state.mongodb_client.close()


async def get_db():
    return app.state.mongodb




@app.get('/list')
async def get_list(session: AsyncSession = Depends(get_async_session)):
    return [await generate_rations(random.randint(14000, 20000), session) for _ in range(10)]


@app.get('/generateRation/{calories}')
async def get_ration(calories: int, session: AsyncSession = Depends(get_async_session)):
    return await generate_rations(calories, session)


@app.get('/products')
async def get_products(session: AsyncSession = Depends(get_async_session)):
    stmt = select(Product)
    res = await session.execute(stmt)
    return [i.name for i in res.scalars().all()]


@app.post('/getRationByIds')
async def get_ration_by_ids(ids: List[str], db=Depends(get_db)):
    object_ids = [ObjectId(id) for id in ids]
    cursor = db["rations"].find({"_id": {"$in": object_ids}})
    items = await cursor.to_list(length=100)
    for item in items:
        item["_id"] = str(item["_id"])
    return items


@app.post('/createRation')
async def create_ration(ration: Ration, db=Depends(get_db)):
    db_item = ration.dict()
    result = await db["rations"].insert_one(db_item)
    return str(result.inserted_id)
