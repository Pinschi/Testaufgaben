import pytest

def volume_of_pyramid(b: float, h: float) -> float:
    """
    Calculates the volume of a square pyramid.
    Uses V = 1/3 * b^2 * h.
    :param b: Length of (square) pyramid base
    :param h: Height of the pyramid
    :return: Volume of the pyramid
    """
    return 1 / 3 * b**2 * h

print(volume_of_pyramid (2,3))

def test_case1_pyramid ():
    result= volume_of_pyramid(1,1)
    assert result == 1/3

def test_case2_pyramid ():
    result= volume_of_pyramid(10,10)
    assert result == 1/3 * 1000

def test_case3_pyramid ():
    result= volume_of_pyramid(3.0001,3.00001)
    assert result == pytest.approx(9, rel=1e-2)