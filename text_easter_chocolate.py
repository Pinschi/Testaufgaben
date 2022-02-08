import pytest
from decimal import Decimal
from datetime import date
from chocolate import calculate_price


_test_data_during_easter_holidays = [
    pytest.param(Decimal('0'), date(2022, 4, 9), Decimal('0.00'), id="Testcase 9"),
    pytest.param(Decimal('0.01'), date(2022, 4, 9), Decimal('0.01'), id="Testcase 10"),
    pytest.param(Decimal('49.99'), date(2022, 4, 9), Decimal('47.49'), id="Testcase 11"),
    pytest.param(Decimal('50'), date(2022, 4, 9), Decimal('47.50'), id="Testcase 12"),
    pytest.param(Decimal('50.01'), date(2022, 4, 9), Decimal('45.01'), id="Testcase 13"),
    pytest.param(Decimal('99.99'), date(2022, 4, 9), Decimal('89.99'), id="Testcase 14"),
    pytest.param(Decimal('100'), date(2022, 4, 9), Decimal('90.00'), id="Testcase 15"),
    pytest.param(Decimal('100.01'), date(2022, 4, 9), Decimal('85.01'), id="Testcase 16"),
    pytest.param(Decimal('0'), date(2022, 4, 18,), Decimal('0.00'), id="Testcase 17"),
    pytest.param(Decimal('0.01'), date(2022, 4, 18), Decimal('0.01'), id="Testcase 18"),
    pytest.param(Decimal('49.99'), date(2022, 4, 18), Decimal('47.49'), id="Testcase 19"),
    pytest.param(Decimal('50'), date(2022, 4, 18), Decimal('47.50'), id="Testcase 20"),
    pytest.param(Decimal('50.01'), date(2022, 4, 18), Decimal('45.01'), id="Testcase 21"),
    pytest.param(Decimal('99.99'), date(2022, 4, 18), Decimal('89.99'), id="Testcase 22"),
    pytest.param(Decimal('100'), date(2022, 4, 18), Decimal('90.00'), id="Testcase 23"),
    pytest.param(Decimal('100.01'), date(2022, 4, 18), Decimal('85.01'), id="Testcase 24"),]


@pytest.mark.parametrize("total,day,expected", _test_data_during_easter_holidays)
def test_prices_during_easter_holidays(total: Decimal, day: date, expected: Decimal):
    # Act
    actual = calculate_price(total, day)
    # Assert
    assert actual == expected


_test_data_outside_easter_holidays = [
    pytest.param(Decimal('0'), date(2022, 4, 8), Decimal('0.00'), id="Testcase 1"),
    pytest.param(Decimal('0.01'), date(2022, 4, 8), Decimal('0.01'), id="Testcase 2"),
    pytest.param(Decimal('49.99'), date(2022, 4, 8), Decimal('49.99'), id="Testcase 3"),
    pytest.param(Decimal('50'), date(2022, 4, 8), Decimal('50'), id="Testcase 4"),
    pytest.param(Decimal('50.01'), date(2022, 4, 8), Decimal('50.01'), id="Testcase 5"),
    pytest.param(Decimal('99.99'), date(2022, 4, 8), Decimal('99.99'), id="Testcase 6"),
    pytest.param(Decimal('100'), date(2022, 4, 8), Decimal('100.00'), id="Testcase 7"),
    pytest.param(Decimal('100.01'), date(2022, 4, 8), Decimal('100.01'), id="Testcase 8"),
    pytest.param(Decimal('0'), date(2022, 4, 19,), Decimal('0.00'), id="Testcase 25"),
    pytest.param(Decimal('0.01'), date(2022, 4, 19), Decimal('0.01'), id="Testcase 26"),
    pytest.param(Decimal('49.99'), date(2022, 4, 19), Decimal('49.99'), id="Testcase 27"),
    pytest.param(Decimal('50'), date(2022, 4, 19), Decimal('50'), id="Testcase 28"),
    pytest.param(Decimal('50.01'), date(2022, 4, 19), Decimal('50.01'), id="Testcase 29"),
    pytest.param(Decimal('99.99'), date(2022, 4, 19), Decimal('99.99'), id="Testcase 20"),
    pytest.param(Decimal('100'), date(2022, 4, 19), Decimal('100.00'), id="Testcase 31"),
    pytest.param(Decimal('100.01'), date(2022, 4, 19), Decimal('100.01'), id="Testcase 32"), ]


@pytest.mark.parametrize("total,day,expected", _test_data_outside_easter_holidays)
def test_prices_outside_easter_holiday(total: Decimal, day: date, expected: Decimal):
    actual = calculate_price(total, day)
    assert actual == expected


_invalid_test_data = [
    pytest.param(Decimal(-0.01), date(2022, 4, 18), id="Testcase 33"),
    pytest.param("abc", date(2022, 4, 18), id="Testcase 34"),
    pytest.param(Decimal('40'), 30, id="Testcase 35")
]


@pytest.mark.parametrize("total,day", _invalid_test_data)
def test_invalid_arguments(total: Decimal, day: date):
    with pytest.raises(ValueError):
        calculate_price(total, day)