import datetime
from typing import Annotated

from sqlalchemy.orm import (
    DeclarativeBase, Mapped, mapped_column, relationship,
    WriteOnlyMapped
)
from sqlalchemy import String, text, ForeignKey, DateTime

int_pk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime.datetime, mapped_column(
    server_default=text("TIMEZONE('utc', now())")
)]
updated_at = Annotated[datetime.datetime, mapped_column(
    server_default=text("TIMEZONE('utc', now())"),
    server_onupdate=text("TIMEZONE('utc', now())"),
    # onupdate=datetime.datetime.now(datetime.UTC),
)]


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'user'

    id: Mapped[int_pk]
    username: Mapped[str] = mapped_column(String(64))
    password: Mapped[str] = mapped_column(String(128))
    is_superuser: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime.datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())")
    )
    session: Mapped['Session'] = relationship(back_populates='user')

    def __repr__(self):
        return f'<User(username={self.username})>'


class Question(Base):
    __tablename__ = 'question'

    id: Mapped[int_pk]
    body: Mapped[str] = mapped_column(String(1024))
    right_answer: Mapped[str] = mapped_column(String(512))
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
    round_id: Mapped[int] = mapped_column(ForeignKey('round.id'), index=True)
    round: Mapped['Round'] = relationship(back_populates='questions')


class Answer(Base):
    __tablename__ = 'answer'

    id: Mapped[int_pk]
    body: Mapped[str] = mapped_column(String(512))
    created_at: Mapped[created_at]


class Round(Base):
    __tablename__ = 'round'

    id: Mapped[int_pk]
    time_to_answer: Mapped[int]
    questions: WriteOnlyMapped['Question'] = relationship(back_populates='round')


class Session(Base):
    __tablename__ = 'session'

    id: Mapped[int_pk]
    session_id: Mapped[str] = mapped_column(unique=True, index=True)
    created_at: Mapped[created_at]
    expires_at: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True))
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), index=True, nullable=False)
    user: Mapped['User'] = relationship(back_populates='session')
