from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from core.models.Base import Base


class User(Base):
    __tablename__ = "users"
    name: Mapped[str] = mapped_column(String, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
