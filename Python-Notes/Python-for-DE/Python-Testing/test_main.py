"""
from main import get_weather

def test_get_weather():
    assert get_weather(21) == 'Hot'
    assert get_weather(18) == 'Cold'
"""

from main import add, divide
import pytest

def test_add():
    assert add(2, 3) == 5,"2 + 3 should be 5"
    assert add(-1, 1) == 0,"-1 + 1 should be 0"
    assert add(0, 0) == 0,"0 + 0 should be 0"

def test_divide():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)

