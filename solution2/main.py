from contextlib import asynccontextmanager

from fastapi import FastAPI
from Users.views import users_router
from core.models.Base import Base
from core.DbHelper import DatabaseHelper, db_helper
import uvicorn

from promos.views import promos_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(lifespan=lifespan)


app.include_router(users_router)
app.include_router(promos_router)


@app.get("/api/ping")
def send():
    return {"status": "ok"}


@app.get("/api/hello/{name}/")
def hello(name: str):
    return f"Hello, { name}!"




if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

"""if __name__ == "__main__":
    host, port = settings.server_address.split(":")
    uvicorn.run(app, host=host, port=int(port))"""
