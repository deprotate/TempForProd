from typing import Annotated, List, Literal, Optional
from pydantic import BaseModel, Field, HttpUrl
from datetime import date


class Target(BaseModel):
    age_from: Annotated[int, Field(ge=0, le=100)]
    age_until: Annotated[int, Field(ge=0, le=100)]
    country: Annotated[Optional[str], Field(min_length=2, max_length=2)] = None
    categories: Annotated[List[str], Field(min_items=1)]


class PromoCreate(BaseModel):
    description: Annotated[str, Field(min_length=10, max_length=300)]
    image_url: Annotated[Optional[HttpUrl], Field(max_length=350)] = None
    target: Target
    max_count: Annotated[int, Field(ge=1, le=100_000_000)]
    active_from: Annotated[date, Field(example="2023-01-01")]
    active_until: Annotated[Optional[date], Field(example="2023-12-31")] = None
    mode: Annotated[Literal["COMMON", "UNIQUE"], Field(description="Режим промокода")]
    promo_common: Annotated[Optional[str], Field(min_length=5, max_length=30)] = None
    promo_unique: Annotated[Optional[List[str]], Field(min_items=1, max_items=5000, example=["winter-sale-30-abc28f99qa"])] = None
