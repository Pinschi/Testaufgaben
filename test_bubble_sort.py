
from bubble_sort import bubble_sort

def test_statement_1():
    assert bubble_sort([]) == []

def test_statement_2():
    assert bubble_sort([8]) == [8]

def test_statement_3():
    assert bubble_sort([8, 7, 5]) == [5,7,8]

def test_statement_4():
    assert bubble_sort([9, 1,5, 4, 2]) == [1,2,4,5,9]