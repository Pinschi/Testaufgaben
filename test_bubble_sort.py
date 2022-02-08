
from bubble_sort import bubble_sort
# tests for statement coverage

def test_statement_1():
    assert bubble_sort([9, 1,5, 4, 2]) == [1,2,4,5,9]


# tests for branch coverage

def test_branch_1():
    assert bubble_sort([]) == []

def test_branch_2():
    assert bubble_sort([8]) == [8]

