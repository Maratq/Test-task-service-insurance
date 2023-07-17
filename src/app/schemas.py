from decimal import Decimal

from pydantic import BaseModel, Field


class Entries(BaseModel):
    rate: float
    cargo_type: str = Field(max_length=255)
    declared_value: Decimal



