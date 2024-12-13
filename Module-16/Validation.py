from typing import Optional
from fastapi import FastAPI, Path
from typing_extensions import Annotated

app = FastAPI()

@app.get('/')
async def welcome() -> str:
    return "Главная страница"

@app.get('/user/admin')
async def admin() -> str:
    return "Вы вошли как администратор"

@app.get('/user/{user_id}')
async def user(user_id: Annotated[int, Path(title="Enter User ID", ge=1, le=100, examples={"example": 1})]) -> str:
    return f"Вы вошли как пользователь № {user_id}"

@app.get('/user/{username}/{age}')
async def user_info(
    username: Annotated[str, Path(title="Enter username", min_length=5, max_length=20, examples={"example": "UrbanUser"})],
    age: Annotated[int, Path(title="Enter age", ge=18, le=120, examples={"example": 24})]
) -> str:
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"
