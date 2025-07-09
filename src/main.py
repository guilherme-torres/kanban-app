from fastapi import FastAPI
from src.infrastructure.api.routes.user import router as user_router
from src.infrastructure.persistence.database.db import Base, engine

Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(user_router)

@app.get("/")
def root():
    return {"message": "hello, World!"}
