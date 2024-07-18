import pytest

from shapes import Square


@pytest.mark.parametrize("side_lenght, expected_area", [(5, 25), (4, 16), (6, 36)])
def test_multiple_square_area(side_lenght, expected_area):
    assert Square(side_lenght).area() == expected_area
    

@pytest.mark.parametrize("side, parameter", [(3, 12), (5, 20), (4, 16)])
def test_multiple_square_parameter(side, parameter):
    assert Square(side).perimeter() == parameter