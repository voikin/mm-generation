from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

MOCK_DATA = [
    {'name': 'Кулич пасхальный от Кухня наизнанку',
     'weight': '1680',
     'calories': '5044',
     'photo': 'https://daily-menu.ru/public/modules/dailymenu/dailymenurecipes/220648/9e8b41832a1c17cdeaac97f8a5fda0e9.jpg',
     'products': [['Цукаты', '50'], ['Изюм кишмиш', '50'], ['Маргарин подсолнечный', '130'], ['Йогурт греческий 10%', '75'], ['Ванильный сахар', '8'], ['Сахар-песок', '150']]},
    {'name': 'Овсяноблин',
     'weight': '112',
     'calories': '221',
     'photo': 'https://daily-menu.ru/public/modules/dailymenu/dailymenurecipes/219346/7bc5c9b39e7486d7fd9c3f55922032ef.jpg',
     'products': [['Яйцо куриное', '55'], ['Мука овсяная', '20'], ['Молоко 2,5% ', '30'], ['Масло подсолнечное', '5'], ['Соль поваренная пищевая', '2']]},
    {'name': 'А-ля лобио',
     'weight': '571',
     'calories': '847',
     'photo': 'https://daily-menu.ru/public/modules/dailymenu/dailymenurecipes/220390/ed329aa3f02a983b568d7a7ffb770877.jpg',
     'products': [['Фасоль красная, консервированная', '425'], ['Масло подсолнечное', '34'], ['Сахар-песок', '7'], ['Уксус 6%', '45'], ['Орех грецкий', '10'], ['Лук репчатый', '50']]}
]


@app.get('/list')
async def get_list():

    return JSONResponse(content=MOCK_DATA, status_code=200)


@app.get('/ration')
async def get_ration():
    return JSONResponse(content=MOCK_DATA[0], status_code=200)
