from typing import Annotated
from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager
from database import create_tables, delete_tables
from router import router as events_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("Creating tables")
    await create_tables()
    print("Tables created!")
    yield
    print("Cleaning up")
    # Clean up the ML models and release the resources


app = FastAPI(lifespan=lifespan)
app.include_router(events_router)






# @app.get("/events")
# async def get_events():
#     events = Event(title="Test", sport_id=1, place="Test", description="Test")
#     return {"events": events}
