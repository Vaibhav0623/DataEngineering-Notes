
import pytest
import my_function as my_function

def test_add():
    result = my_function.add(1, 4)
    assert result == 5

def test_add_string():
    result = my_function.add("i like ", "daal bati")
    assert result == "i like daal bati"
    
def test_divide():
    result = my_function.divide(10, 5)
    assert result == 2

def test_divide_by_zero():
    with pytest.raises(ValueError):
        my_function.divide(8, 0)




