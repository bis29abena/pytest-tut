import pytest
from shapes import  Rectangle


@pytest.fixture
def my_rectangle():
    return Rectangle(10, 2)


@pytest.fixture
def weird_rectangle():
    return Rectangle(10, 3)