import pytest

from calculator import square


def test_positive_square():
    assert square(2) == 4
    assert square(3) == 9
    print("test_positive_square")
    
def test_negative_square():
    assert square(-2) == 4
    assert square(-3) == 9
    print("test_negative_square")
    
def test_zero_square():
    assert square(0) == 0
    print("test_zero_square")
    
def test_string_square():
    with pytest.raises(TypeError):
        square("cat")
    print("test_string_square")
        
def main():
    test_positive_square()
    test_negative_square()
    test_zero_square()
    test_string_square()
    
main()