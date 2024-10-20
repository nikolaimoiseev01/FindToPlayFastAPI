from typing import Annotated
from fastapi import Depends
from repository import EventRepository
from schemas import SEventAdd, SEvent
from fastapi import APIRouter

router = APIRouter(
    prefix="/events",
    tags=["События"],
)


@router.get("")
async def get_events() -> list[SEvent]:
    events = await EventRepository.get_events()
    return events


@router.post("")
async def create_event(
    event: Annotated[SEventAdd, Depends()]
):
    event_id = await EventRepository.create_event(data=event)
    return {"id": event_id}
