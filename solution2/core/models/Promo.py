from typing import Optional

from sqlalchemy import Integer, String, Date, JSON
from sqlalchemy.orm import Mapped, mapped_column
from core.models.Base import Base


class Promo(Base):
    __tablename__ = "promos"

    description: Mapped[str] = mapped_column(String(300), nullable=False)
    image_url: Mapped[Optional[str]] = mapped_column(String(350))
    target: Mapped[dict] = mapped_column(JSON, nullable=False)
    max_count: Mapped[int] = mapped_column(Integer, nullable=False)
    active_from: Mapped[Date] = mapped_column(nullable=False)
    active_until: Mapped[Optional[Date]]
    mode: Mapped[str] = mapped_column(String(10), nullable=False)
    promo_common: Mapped[Optional[str]] = mapped_column(String(30))
    promo_unique: Mapped[Optional[list]] = mapped_column(JSON)
