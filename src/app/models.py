from datetime import date

from tortoise import fields
from tortoise.models import Model


class Entry(Model):
    id = fields.IntField(pk=True)
    date = fields.DateField(default=date.today)
    cargo_type = fields.CharField(max_length=255)
    rate = fields.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        table = "Entry"
