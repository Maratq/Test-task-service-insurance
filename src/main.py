from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from src.app.router import router
from src.config import DB_CONNECTION

app = FastAPI()


def connection_database():
    register_tortoise(
        app,
        db_url=DB_CONNECTION,
        modules={'models': ['src.app.models']},
        generate_schemas=True,
        add_exception_handlers=True
    )


connection_database()

app.include_router(router)
