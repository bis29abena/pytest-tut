import pytest
import my_functions
import time

def test_add():
    
    result = my_functions.add(1, 4)
    
    assert result == 5
    
def test_add_strings():
    result = my_functions.add("Hello ", "World")
    
    assert result == "Hello World"
    
def test_divide():
    result = my_functions.divide(10, 2)
    
    assert result == 5
    
def test_divide_zero():
    
    with pytest.raises(ValueError):
        my_functions.divide(10, 0)
    
   
# @pytest.mark.slow   
# def test_very_slow():
#     time.sleep(5)
#     result = my_functions.divide(10, 5)
    
#     assert result == 2
    
    
@pytest.mark.skip(reason="This feature is currently broken")
def test_add_more():
    assert my_functions.add(1, 3) == 4
    
@pytest.mark.xfail(reason="We know this feature no longer exist")
def test_devide_zero_broken():
    my_functions.divide(4,0)