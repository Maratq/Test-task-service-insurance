import json
from datetime import date

from _decimal import Decimal
from fastapi import APIRouter, HTTPException
from pydantic import ValidationError

from src.app.models import Entry

router = APIRouter()


@router.post("/calculate_insurance")
async def calculate_insurance(cargo_type: str, declared_value: Decimal, date: str):
    cargo = await Entry.filter(cargo_type=cargo_type).first()
    if not cargo:
        raise HTTPException(status_code=404, detail="Cargo type not found")

    insurance_cost = declared_value * cargo.rate

    return {"insurance_cost": insurance_cost}


@router.post("/load_tariff")
async def load_tariff():
    try:
        with open("tariff.json") as file:
            tariff_data = json.load(file)
            for date_str, cargo_rates in tariff_data.items():
                for cargo_rate in cargo_rates:
                    new_tariff = await Entry.create(
                        date=date.fromisoformat(date_str),
                        cargo_type=cargo_rate["cargo_type"],
                        rate=cargo_rate["rate"],
                    )

        return {"message": "Tariff loaded successfully"}
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=str(e))
