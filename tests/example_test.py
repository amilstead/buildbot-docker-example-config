import pytest


@pytest.fixture()
def a_string():
    return "a string"


def test_equality(a_string):
    assert a_string == "hello string"
