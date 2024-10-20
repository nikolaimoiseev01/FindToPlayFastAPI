from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, sessionmaker, mapped_column, relationship, Mapped

engine = create_async_engine('sqlite+aiosqlite:///database.db')

new_session = async_sessionmaker(engine, expire_on_commit=False)


class Model(DeclarativeBase):
    pass


class EventsTable(Model):
    __tablename__ = 'events'

    id: Mapped[int] = mapped_column(primary_key=True)
    sport_id: Mapped[int]
    title: Mapped[str]
    description: Mapped[str]
    place: Mapped[str]


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync (Model.metadata.create_all)


async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync (Model.metadata.drop_all)
