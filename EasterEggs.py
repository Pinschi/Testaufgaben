from decimal import Decimal
from datetime import date

def calculate_price (total: Decimal, day: date ):
    return Decimal (total)


def test_calculate_price_4():
    assert calculate_price(Decimal("0.01"), date ( 2022, 4, 8)) == Decimal ("0.01")