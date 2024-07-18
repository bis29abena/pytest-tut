import pytest

from shapes import Shape, Circle
import math


class TestCircle:
    pass

    def setup_method(self, method):
        self.circle = Circle(10)
        
    def teardown_method(self, method):
        del self.circle

    def test_area(self):
        
        assert self.circle.area() == math.pi * self.circle.radius ** 2
        
    def test_perimeter(self):
        result = self.circle.perimeter()
        
        expected_value = 2 * math.pi * self.circle.radius
        
        assert result == expected_value
        