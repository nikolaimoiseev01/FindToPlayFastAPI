from pydantic import BaseModel


class SEventAdd(BaseModel):
    title: str
    sport_id: int
    place: str
    description: str


class SEvent(SEventAdd):
    id: int
