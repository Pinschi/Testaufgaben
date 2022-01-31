import pytest
def calculate_discount(amount: int, member: bool) -> float:
    """
    Calculates the discount for a purchase of juice depending on the amount a customer purchases and whether she is a
    bonus club member.
    :param amount: The amount of juice cartons the customer purchases
    :param member: Whether the customer is a bonus club member
    :return: The discount between 0 and 1
    :raises:
        ValueError: if amount is not an integer or not within the accepted range, e.g., 0 < amount <= 10
    """

    if not isinstance(amount, int):
        raise ValueError("amount must be an int")
    if amount < 1 or amount > 10:
        raise ValueError("amount has to be greater than 0 and less or equal to 10")

    percentages = {(1, 2): 1.0, (3, 3): 3 / 4, (4, 5): 2 / 3, (6, 10): 1 / 2}

    for interval, percentage in percentages.items():
        if interval[0] <= amount <= interval[1]:
            if member:
                percentage *= 4 / 5

            return 1 - percentage

    raise RuntimeError("Logical error. Check implementation.")



def test_case1_juice ():
    assert calculate_discount(1,True) == pytest.approx(0.2, rel=1e-2)

def test_case2_juice ():
    result= calculate_discount(2,True)
    assert result == pytest.approx(0.2, rel=1e-2)

def test_case3_juice ():
    result= calculate_discount(1,False)
    assert result == 0

def test_case4_juice ():
    result= calculate_discount(2,False)
    assert result == 0

def test_case5_juice ():
    result= calculate_discount(3,True)
    assert result == pytest.approx(0.4, rel=1e-2)

def test_case6_juice ():
    result= calculate_discount(3,False)
    assert result == 0.25

def test_case7_juice ():
    result= calculate_discount(4,True)
    assert result == pytest.approx(0.46, rel=1e-1)

def test_case8_juice ():
    result= calculate_discount(5,True)
    assert result == pytest.approx(0.46, rel=1e-1)

def test_case9_juice ():
    result= calculate_discount(4,False)
    assert result == pytest.approx(0.33, rel=1e-1)

def test_case10_juice ():
    result= calculate_discount(5,False)
    assert result == pytest.approx(0.33, rel=1e-1)

def test_case11_juice ():
    result= calculate_discount(6,True)
    assert result == pytest.approx(0.6, rel=1e-1)

def test_case12_juice ():
    result= calculate_discount(10,True)
    assert result == pytest.approx(0.6, rel=1e-1)

def test_case13_juice ():
    result= calculate_discount(6,False)
    assert result == 0.5

def test_case14_juice ():
    result= calculate_discount(10,False)
    assert result == 0.5


def test_expect_error_1():
    with pytest.raises(ValueError) as exception_info:
        calculate_discount(11,False)
    assert str(exception_info.value) == "amount has to be greater than 0 and less or equal to 10"
    assert exception_info.type == ValueError

def test_expect_error_2():
    with pytest.raises(ValueError) as exception_info:
        calculate_discount(0,True)
    assert str(exception_info.value) == "amount has to be greater than 0 and less or equal to 10"
    assert exception_info.type == ValueError

def test_expect_error_3():
    with pytest.raises(ValueError) as exception_info:
        calculate_discount(2.5,False)
    assert str(exception_info.value) == "amount must be an int"
    assert exception_info.type == ValueError

def test_expect_error_4():
    with pytest.raises(ValueError) as exception_info:
        calculate_discount("test",True)
    assert str(exception_info.value) == "amount must be an int"
    assert exception_info.type == ValueError

    
