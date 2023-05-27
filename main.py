from bson import ObjectId
from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from motor.motor_asyncio import AsyncIOMotorClient

from schemas import Ids, Ration
from settings import mongo_uri

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

MOCK_DATA = [
    {
        "monday":
            [
                {
                    'name': 'Кулич пасхальный от Кухня наизнанку',
                    'weight': '1680',
                    'calories': '5044',
                    'photo': 'https://daily-menu.ru/public/modules/dailymenu/dailymenurecipes/220648/9e8b41832a1c17cdeaac97f8a5fda0e9.jpg',
                    'products': [['Цукаты', '50'], ['Изюм кишмиш', '50'], ['Маргарин подсолнечный', '130'], ['Йогурт греческий 10%', '75'], ['Ванильный сахар', '8'], ['Сахар-песок', '150']]
                },
                {
                    'name': 'Овсяноблин',
                    'weight': '112',
                    'calories': '221',
                    'photo': 'https://daily-menu.ru/public/modules/dailymenu/dailymenurecipes/219346/7bc5c9b39e7486d7fd9c3f55922032ef.jpg',
                    'products': [['Яйцо куриное', '55'], ['Мука овсяная', '20'], ['Молоко 2,5% ', '30'], ['Масло подсолнечное', '5'], ['Соль поваренная пищевая', '2']]
                },
                {
                    'name': 'А-ля лобио',
                    'weight': '571',
                    'calories': '847',
                    'photo': 'https://daily-menu.ru/public/modules/dailymenu/dailymenurecipes/220390/ed329aa3f02a983b568d7a7ffb770877.jpg',
                    'products': [['Фасоль красная, консервированная', '425'], ['Масло подсолнечное', '34'], ['Сахар-песок', '7'], ['Уксус 6%', '45'], ['Орех грецкий', '10'], ['Лук репчатый', '50']]
                }
            ],
        "tuesday":
            [
                {
                    'name': 'Кулич пасхальный от Кухня наизнанку',
                    'weight': '1680',
                    'calories': '5044',
                    'photo': 'https://daily-menu.ru/public/modules/dailymenu/dailymenurecipes/220648/9e8b41832a1c17cdeaac97f8a5fda0e9.jpg',
                    'products': [['Цукаты', '50'], ['Изюм кишмиш', '50'], ['Маргарин подсолнечный', '130'], ['Йогурт греческий 10%', '75'], ['Ванильный сахар', '8'], ['Сахар-песок', '150']]
                },
                {
                    'name': 'Овсяноблин',
                    'weight': '112',
                    'calories': '221',
                    'photo': 'https://daily-menu.ru/public/modules/dailymenu/dailymenurecipes/219346/7bc5c9b39e7486d7fd9c3f55922032ef.jpg',
                    'products': [['Яйцо куриное', '55'], ['Мука овсяная', '20'], ['Молоко 2,5% ', '30'], ['Масло подсолнечное', '5'], ['Соль поваренная пищевая', '2']]
                },
                {
                    'name': 'А-ля лобио',
                    'weight': '571',
                    'calories': '847',
                    'photo': 'https://daily-menu.ru/public/modules/dailymenu/dailymenurecipes/220390/ed329aa3f02a983b568d7a7ffb770877.jpg',
                    'products': [['Фасоль красная, консервированная', '425'], ['Масло подсолнечное', '34'], ['Сахар-песок', '7'], ['Уксус 6%', '45'], ['Орех грецкий', '10'], ['Лук репчатый', '50']]
                }
            ],
        "wednesday":
            [
                {
                    'name': 'Кулич пасхальный от Кухня наизнанку',
                    'weight': '1680',
                    'calories': '5044',
                    'photo': 'https://daily-menu.ru/public/modules/dailymenu/dailymenurecipes/220648/9e8b41832a1c17cdeaac97f8a5fda0e9.jpg',
                    'products': [['Цукаты', '50'], ['Изюм кишмиш', '50'], ['Маргарин подсолнечный', '130'], ['Йогурт греческий 10%', '75'], ['Ванильный сахар', '8'], ['Сахар-песок', '150']]
                },
                {
                    'name': 'Овсяноблин',
                    'weight': '112',
                    'calories': '221',
                    'photo': 'https://daily-menu.ru/public/modules/dailymenu/dailymenurecipes/219346/7bc5c9b39e7486d7fd9c3f55922032ef.jpg',
                    'products': [['Яйцо куриное', '55'], ['Мука овсяная', '20'], ['Молоко 2,5% ', '30'], ['Масло подсолнечное', '5'], ['Соль поваренная пищевая', '2']]
                },
                {
                    'name': 'А-ля лобио',
                    'weight': '571',
                    'calories': '847',
                    'photo': 'https://daily-menu.ru/public/modules/dailymenu/dailymenurecipes/220390/ed329aa3f02a983b568d7a7ffb770877.jpg',
                    'products': [['Фасоль красная, консервированная', '425'], ['Масло подсолнечное', '34'], ['Сахар-песок', '7'], ['Уксус 6%', '45'], ['Орех грецкий', '10'], ['Лук репчатый', '50']]
                }
            ],
        "thursday":
            [
                {
                    'name': 'Кулич пасхальный от Кухня наизнанку',
                    'weight': '1680',
                    'calories': '5044',
                    'photo': 'https://daily-menu.ru/public/modules/dailymenu/dailymenurecipes/220648/9e8b41832a1c17cdeaac97f8a5fda0e9.jpg',
                    'products': [['Цукаты', '50'], ['Изюм кишмиш', '50'], ['Маргарин подсолнечный', '130'], ['Йогурт греческий 10%', '75'], ['Ванильный сахар', '8'], ['Сахар-песок', '150']]
                },
                {
                    'name': 'Овсяноблин',
                    'weight': '112',
                    'calories': '221',
                    'photo': 'https://daily-menu.ru/public/modules/dailymenu/dailymenurecipes/219346/7bc5c9b39e7486d7fd9c3f55922032ef.jpg',
                    'products': [['Яйцо куриное', '55'], ['Мука овсяная', '20'], ['Молоко 2,5% ', '30'], ['Масло подсолнечное', '5'], ['Соль поваренная пищевая', '2']]
                },
                {
                    'name': 'А-ля лобио',
                    'weight': '571',
                    'calories': '847',
                    'photo': 'https://daily-menu.ru/public/modules/dailymenu/dailymenurecipes/220390/ed329aa3f02a983b568d7a7ffb770877.jpg',
                    'products': [['Фасоль красная, консервированная', '425'], ['Масло подсолнечное', '34'], ['Сахар-песок', '7'], ['Уксус 6%', '45'], ['Орех грецкий', '10'], ['Лук репчатый', '50']]
                }
            ],
        "friday":
            [
                {
                    'name': 'Кулич пасхальный от Кухня наизнанку',
                    'weight': '1680',
                    'calories': '5044',
                    'photo': 'https://daily-menu.ru/public/modules/dailymenu/dailymenurecipes/220648/9e8b41832a1c17cdeaac97f8a5fda0e9.jpg',
                    'products': [['Цукаты', '50'], ['Изюм кишмиш', '50'], ['Маргарин подсолнечный', '130'], ['Йогурт греческий 10%', '75'], ['Ванильный сахар', '8'], ['Сахар-песок', '150']]
                },
                {
                    'name': 'Овсяноблин',
                    'weight': '112',
                    'calories': '221',
                    'photo': 'https://daily-menu.ru/public/modules/dailymenu/dailymenurecipes/219346/7bc5c9b39e7486d7fd9c3f55922032ef.jpg',
                    'products': [['Яйцо куриное', '55'], ['Мука овсяная', '20'], ['Молоко 2,5% ', '30'], ['Масло подсолнечное', '5'], ['Соль поваренная пищевая', '2']]
                },
                {
                    'name': 'А-ля лобио',
                    'weight': '571',
                    'calories': '847',
                    'photo': 'https://daily-menu.ru/public/modules/dailymenu/dailymenurecipes/220390/ed329aa3f02a983b568d7a7ffb770877.jpg',
                    'products': [['Фасоль красная, консервированная', '425'], ['Масло подсолнечное', '34'], ['Сахар-песок', '7'], ['Уксус 6%', '45'], ['Орех грецкий', '10'], ['Лук репчатый', '50']]
                }
            ],
        "saturday":
            [
                {
                    'name': 'Кулич пасхальный от Кухня наизнанку',
                    'weight': '1680',
                    'calories': '5044',
                    'photo': 'https://daily-menu.ru/public/modules/dailymenu/dailymenurecipes/220648/9e8b41832a1c17cdeaac97f8a5fda0e9.jpg',
                    'products': [['Цукаты', '50'], ['Изюм кишмиш', '50'], ['Маргарин подсолнечный', '130'], ['Йогурт греческий 10%', '75'], ['Ванильный сахар', '8'], ['Сахар-песок', '150']]
                },
                {
                    'name': 'Овсяноблин',
                    'weight': '112',
                    'calories': '221',
                    'photo': 'https://daily-menu.ru/public/modules/dailymenu/dailymenurecipes/219346/7bc5c9b39e7486d7fd9c3f55922032ef.jpg',
                    'products': [['Яйцо куриное', '55'], ['Мука овсяная', '20'], ['Молоко 2,5% ', '30'], ['Масло подсолнечное', '5'], ['Соль поваренная пищевая', '2']]
                },
                {
                    'name': 'А-ля лобио',
                    'weight': '571',
                    'calories': '847',
                    'photo': 'https://daily-menu.ru/public/modules/dailymenu/dailymenurecipes/220390/ed329aa3f02a983b568d7a7ffb770877.jpg',
                    'products': [['Фасоль красная, консервированная', '425'], ['Масло подсолнечное', '34'], ['Сахар-песок', '7'], ['Уксус 6%', '45'], ['Орех грецкий', '10'], ['Лук репчатый', '50']]
                }
            ],
        "sunday":
            [
                {
                    'name': 'Кулич пасхальный от Кухня наизнанку',
                    'weight': '1680',
                    'calories': '5044',
                    'photo': 'https://daily-menu.ru/public/modules/dailymenu/dailymenurecipes/220648/9e8b41832a1c17cdeaac97f8a5fda0e9.jpg',
                    'products': [['Цукаты', '50'], ['Изюм кишмиш', '50'], ['Маргарин подсолнечный', '130'], ['Йогурт греческий 10%', '75'], ['Ванильный сахар', '8'], ['Сахар-песок', '150']]
                },
                {
                    'name': 'Овсяноблин',
                    'weight': '112',
                    'calories': '221',
                    'photo': 'https://daily-menu.ru/public/modules/dailymenu/dailymenurecipes/219346/7bc5c9b39e7486d7fd9c3f55922032ef.jpg',
                    'products': [['Яйцо куриное', '55'], ['Мука овсяная', '20'], ['Молоко 2,5% ', '30'], ['Масло подсолнечное', '5'], ['Соль поваренная пищевая', '2']]
                },
                {
                    'name': 'А-ля лобио',
                    'weight': '571',
                    'calories': '847',
                    'photo': 'https://daily-menu.ru/public/modules/dailymenu/dailymenurecipes/220390/ed329aa3f02a983b568d7a7ffb770877.jpg',
                    'products': [['Фасоль красная, консервированная', '425'], ['Масло подсолнечное', '34'], ['Сахар-песок', '7'], ['Уксус 6%', '45'], ['Орех грецкий', '10'], ['Лук репчатый', '50']]
                }
            ]
    },
    {
        "monday":
            [
                {
                    'name': 'Кулич пасхальный от Кухня наизнанку',
                    'weight': '1680',
                    'calories': '5044',
                    'photo': 'https://daily-menu.ru/public/modules/dailymenu/dailymenurecipes/220648/9e8b41832a1c17cdeaac97f8a5fda0e9.jpg',
                    'products': [['Цукаты', '50'], ['Изюм кишмиш', '50'], ['Маргарин подсолнечный', '130'], ['Йогурт греческий 10%', '75'], ['Ванильный сахар', '8'], ['Сахар-песок', '150']]
                },
                {
                    'name': 'Овсяноблин',
                    'weight': '112',
                    'calories': '221',
                    'photo': 'https://daily-menu.ru/public/modules/dailymenu/dailymenurecipes/219346/7bc5c9b39e7486d7fd9c3f55922032ef.jpg',
                    'products': [['Яйцо куриное', '55'], ['Мука овсяная', '20'], ['Молоко 2,5% ', '30'], ['Масло подсолнечное', '5'], ['Соль поваренная пищевая', '2']]
                },
                {
                    'name': 'А-ля лобио',
                    'weight': '571',
                    'calories': '847',
                    'photo': 'https://daily-menu.ru/public/modules/dailymenu/dailymenurecipes/220390/ed329aa3f02a983b568d7a7ffb770877.jpg',
                    'products': [['Фасоль красная, консервированная', '425'], ['Масло подсолнечное', '34'], ['Сахар-песок', '7'], ['Уксус 6%', '45'], ['Орех грецкий', '10'], ['Лук репчатый', '50']]
                }
            ],
        "tuesday":
            [
                {
                    'name': 'Кулич пасхальный от Кухня наизнанку',
                    'weight': '1680',
                    'calories': '5044',
                    'photo': 'https://daily-menu.ru/public/modules/dailymenu/dailymenurecipes/220648/9e8b41832a1c17cdeaac97f8a5fda0e9.jpg',
                    'products': [['Цукаты', '50'], ['Изюм кишмиш', '50'], ['Маргарин подсолнечный', '130'], ['Йогурт греческий 10%', '75'], ['Ванильный сахар', '8'], ['Сахар-песок', '150']]
                },
                {
                    'name': 'Овсяноблин',
                    'weight': '112',
                    'calories': '221',
                    'photo': 'https://daily-menu.ru/public/modules/dailymenu/dailymenurecipes/219346/7bc5c9b39e7486d7fd9c3f55922032ef.jpg',
                    'products': [['Яйцо куриное', '55'], ['Мука овсяная', '20'], ['Молоко 2,5% ', '30'], ['Масло подсолнечное', '5'], ['Соль поваренная пищевая', '2']]
                },
                {
                    'name': 'А-ля лобио',
                    'weight': '571',
                    'calories': '847',
                    'photo': 'https://daily-menu.ru/public/modules/dailymenu/dailymenurecipes/220390/ed329aa3f02a983b568d7a7ffb770877.jpg',
                    'products': [['Фасоль красная, консервированная', '425'], ['Масло подсолнечное', '34'], ['Сахар-песок', '7'], ['Уксус 6%', '45'], ['Орех грецкий', '10'], ['Лук репчатый', '50']]
                }
            ],
        "wednesday":
            [
                {
                    'name': 'Кулич пасхальный от Кухня наизнанку',
                    'weight': '1680',
                    'calories': '5044',
                    'photo': 'https://daily-menu.ru/public/modules/dailymenu/dailymenurecipes/220648/9e8b41832a1c17cdeaac97f8a5fda0e9.jpg',
                    'products': [['Цукаты', '50'], ['Изюм кишмиш', '50'], ['Маргарин подсолнечный', '130'], ['Йогурт греческий 10%', '75'], ['Ванильный сахар', '8'], ['Сахар-песок', '150']]
                },
                {
                    'name': 'Овсяноблин',
                    'weight': '112',
                    'calories': '221',
                    'photo': 'https://daily-menu.ru/public/modules/dailymenu/dailymenurecipes/219346/7bc5c9b39e7486d7fd9c3f55922032ef.jpg',
                    'products': [['Яйцо куриное', '55'], ['Мука овсяная', '20'], ['Молоко 2,5% ', '30'], ['Масло подсолнечное', '5'], ['Соль поваренная пищевая', '2']]
                },
                {
                    'name': 'А-ля лобио',
                    'weight': '571',
                    'calories': '847',
                    'photo': 'https://daily-menu.ru/public/modules/dailymenu/dailymenurecipes/220390/ed329aa3f02a983b568d7a7ffb770877.jpg',
                    'products': [['Фасоль красная, консервированная', '425'], ['Масло подсолнечное', '34'], ['Сахар-песок', '7'], ['Уксус 6%', '45'], ['Орех грецкий', '10'], ['Лук репчатый', '50']]
                }
            ],
        "thursday":
            [
                {
                    'name': 'Кулич пасхальный от Кухня наизнанку',
                    'weight': '1680',
                    'calories': '5044',
                    'photo': 'https://daily-menu.ru/public/modules/dailymenu/dailymenurecipes/220648/9e8b41832a1c17cdeaac97f8a5fda0e9.jpg',
                    'products': [['Цукаты', '50'], ['Изюм кишмиш', '50'], ['Маргарин подсолнечный', '130'], ['Йогурт греческий 10%', '75'], ['Ванильный сахар', '8'], ['Сахар-песок', '150']]
                },
                {
                    'name': 'Овсяноблин',
                    'weight': '112',
                    'calories': '221',
                    'photo': 'https://daily-menu.ru/public/modules/dailymenu/dailymenurecipes/219346/7bc5c9b39e7486d7fd9c3f55922032ef.jpg',
                    'products': [['Яйцо куриное', '55'], ['Мука овсяная', '20'], ['Молоко 2,5% ', '30'], ['Масло подсолнечное', '5'], ['Соль поваренная пищевая', '2']]
                },
                {
                    'name': 'А-ля лобио',
                    'weight': '571',
                    'calories': '847',
                    'photo': 'https://daily-menu.ru/public/modules/dailymenu/dailymenurecipes/220390/ed329aa3f02a983b568d7a7ffb770877.jpg',
                    'products': [['Фасоль красная, консервированная', '425'], ['Масло подсолнечное', '34'], ['Сахар-песок', '7'], ['Уксус 6%', '45'], ['Орех грецкий', '10'], ['Лук репчатый', '50']]
                }
            ],
        "friday":
            [
                {
                    'name': 'Кулич пасхальный от Кухня наизнанку',
                    'weight': '1680',
                    'calories': '5044',
                    'photo': 'https://daily-menu.ru/public/modules/dailymenu/dailymenurecipes/220648/9e8b41832a1c17cdeaac97f8a5fda0e9.jpg',
                    'products': [['Цукаты', '50'], ['Изюм кишмиш', '50'], ['Маргарин подсолнечный', '130'], ['Йогурт греческий 10%', '75'], ['Ванильный сахар', '8'], ['Сахар-песок', '150']]
                },
                {
                    'name': 'Овсяноблин',
                    'weight': '112',
                    'calories': '221',
                    'photo': 'https://daily-menu.ru/public/modules/dailymenu/dailymenurecipes/219346/7bc5c9b39e7486d7fd9c3f55922032ef.jpg',
                    'products': [['Яйцо куриное', '55'], ['Мука овсяная', '20'], ['Молоко 2,5% ', '30'], ['Масло подсолнечное', '5'], ['Соль поваренная пищевая', '2']]
                },
                {
                    'name': 'А-ля лобио',
                    'weight': '571',
                    'calories': '847',
                    'photo': 'https://daily-menu.ru/public/modules/dailymenu/dailymenurecipes/220390/ed329aa3f02a983b568d7a7ffb770877.jpg',
                    'products': [['Фасоль красная, консервированная', '425'], ['Масло подсолнечное', '34'], ['Сахар-песок', '7'], ['Уксус 6%', '45'], ['Орех грецкий', '10'], ['Лук репчатый', '50']]
                }
            ],
        "saturday":
            [
                {
                    'name': 'Кулич пасхальный от Кухня наизнанку',
                    'weight': '1680',
                    'calories': '5044',
                    'photo': 'https://daily-menu.ru/public/modules/dailymenu/dailymenurecipes/220648/9e8b41832a1c17cdeaac97f8a5fda0e9.jpg',
                    'products': [['Цукаты', '50'], ['Изюм кишмиш', '50'], ['Маргарин подсолнечный', '130'], ['Йогурт греческий 10%', '75'], ['Ванильный сахар', '8'], ['Сахар-песок', '150']]
                },
                {
                    'name': 'Овсяноблин',
                    'weight': '112',
                    'calories': '221',
                    'photo': 'https://daily-menu.ru/public/modules/dailymenu/dailymenurecipes/219346/7bc5c9b39e7486d7fd9c3f55922032ef.jpg',
                    'products': [['Яйцо куриное', '55'], ['Мука овсяная', '20'], ['Молоко 2,5% ', '30'], ['Масло подсолнечное', '5'], ['Соль поваренная пищевая', '2']]
                },
                {
                    'name': 'А-ля лобио',
                    'weight': '571',
                    'calories': '847',
                    'photo': 'https://daily-menu.ru/public/modules/dailymenu/dailymenurecipes/220390/ed329aa3f02a983b568d7a7ffb770877.jpg',
                    'products': [['Фасоль красная, консервированная', '425'], ['Масло подсолнечное', '34'], ['Сахар-песок', '7'], ['Уксус 6%', '45'], ['Орех грецкий', '10'], ['Лук репчатый', '50']]
                }
            ],
        "sunday":
            [
                {
                    'name': 'Кулич пасхальный от Кухня наизнанку',
                    'weight': '1680',
                    'calories': '5044',
                    'photo': 'https://daily-menu.ru/public/modules/dailymenu/dailymenurecipes/220648/9e8b41832a1c17cdeaac97f8a5fda0e9.jpg',
                    'products': [['Цукаты', '50'], ['Изюм кишмиш', '50'], ['Маргарин подсолнечный', '130'], ['Йогурт греческий 10%', '75'], ['Ванильный сахар', '8'], ['Сахар-песок', '150']]
                },
                {
                    'name': 'Овсяноблин',
                    'weight': '112',
                    'calories': '221',
                    'photo': 'https://daily-menu.ru/public/modules/dailymenu/dailymenurecipes/219346/7bc5c9b39e7486d7fd9c3f55922032ef.jpg',
                    'products': [['Яйцо куриное', '55'], ['Мука овсяная', '20'], ['Молоко 2,5% ', '30'], ['Масло подсолнечное', '5'], ['Соль поваренная пищевая', '2']]
                },
                {
                    'name': 'А-ля лобио',
                    'weight': '571',
                    'calories': '847',
                    'photo': 'https://daily-menu.ru/public/modules/dailymenu/dailymenurecipes/220390/ed329aa3f02a983b568d7a7ffb770877.jpg',
                    'products': [['Фасоль красная, консервированная', '425'], ['Масло подсолнечное', '34'], ['Сахар-песок', '7'], ['Уксус 6%', '45'], ['Орех грецкий', '10'], ['Лук репчатый', '50']]
                }
            ]
    },

]


@app.get('/list')
async def get_list():

    return JSONResponse(content=MOCK_DATA, status_code=200)


@app.get('/generateRation')
async def get_ration():
    return JSONResponse(content=MOCK_DATA[0], status_code=200)


@app.post('/getRationByIds')
async def get_ration_by_ids(ids: Ids, db=Depends(get_db)):
    object_ids = [ObjectId(id) for id in ids.ids]
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

