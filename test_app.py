# test_app.py

  
from app import add, multiply, divide
import pytest

def test_add_positive_numbers():
    assert add(1, 2) == 3

def test_add_negative_numbers():
    assert add(-1, -1) == -2

def test_multiply():
    assert multiply(3, 4) == 12

def test_divide_valid():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    # This checks if the function correctly raises an error
    with pytest.raises(ValueError):
        divide(10, 0)
