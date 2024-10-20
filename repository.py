from sqlalchemy import select

from database import new_session, EventsTable
from schemas import SEventAdd, SEvent


class EventRepository:
    @classmethod
    async def get_events(cls) -> list[SEvent]:
        async with new_session() as session:
            query = select(EventsTable)
            result = await session.execute(query)
            event_models = result.scalars().all()
            event_schemas = [SEvent.model_validate(event) for event in event_models]
            return event_schemas

    @classmethod
    async def create_event(cls, data: SEventAdd) -> int:
       async with new_session() as session:
           event_dict = data.model_dump()
           event = EventsTable(**event_dict)
           session.add(event)
           await session.flush()
           await session.commit()
           return event.id
