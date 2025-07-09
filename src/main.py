from fastapi import FastAPI
from src.infrastructure.persistence.database.db import Base, engine
from src.infrastructure.api.routes.user import router as user_router
from src.infrastructure.api.routes.status import router as status_router
from src.infrastructure.api.routes.task import router as task_router

Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(user_router)
app.include_router(status_router)
app.include_router(task_router)

@app.get("/")
def root():
    return {"message": "hello, World!"}
