from typing import Dict, List

from pydantic import BaseModel, Field
from decimal import Decimal


class Entries(BaseModel):
    rate: float
    cargo_type: str = Field(max_length=255)
    declared_value: Decimal



