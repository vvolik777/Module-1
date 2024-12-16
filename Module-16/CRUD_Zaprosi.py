from typing import Dict
from fastapi import FastAPI, Path
from typing_extensions import Annotated


app = FastAPI()

users: Dict[str, str] = {'1': 'Имя: Example, возраст: 18'}

@app.get('/users')
async def get_users() -> Dict[str, str]:
    return users

@app.post('/user/{username}/{age}')
async def post_user(
    username: Annotated[str, Path(title="Enter username", min_length=1, max_length=50)],
    age: Annotated[int, Path(title="Enter age", ge=0, le=120)]) -> str:

    new_id = str(max(map(int, users.keys())) + 1) if users else '1'
    users[new_id] = f"Имя: {username}, возраст: {age}"
    return f"User {new_id} is registered"

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(
    user_id: Annotated[str, Path(title="Enter User ID")],
    username: Annotated[str, Path(title="Enter username", min_length=1, max_length=50)],
    age: Annotated[int, Path(title="Enter age", ge=0, le=120)] ) -> str:

    if user_id not in users:
        return f"User {user_id} not found"
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} has been updated"


@app.delete('/user/{user_id}')
async def delete_user(user_id: Annotated[str, Path(title="Enter User ID")]) -> str:
    if user_id not in users:
        return f"User {user_id} not found"
    del users[user_id]
    return f"User {user_id} has been deleted"
