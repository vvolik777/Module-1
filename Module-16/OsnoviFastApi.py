from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def welcome():
    return  "Главная страница"


@app.get('/user/admin')
async def admin():
    return  "Вы вошли как администратор"


@app.get('/user/{user_id}')
async def user(user_id: int):
    return  f"Вы вошли как пользователь № {user_id}"


@app.get('/user')
async def user_info(username: Optional[str] = "Гость", age: Optional[int] = 0):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"
