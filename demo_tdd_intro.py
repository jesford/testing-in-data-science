"""
Demo 1: Intro to Testing in Data Science

Practice TDD - write the test before modifying the code;
check that the test fails; write code to make it pass.

TDD Tasks (one at a time):
1. whitespace should be removed from any input text
2. punctuation should also be removed
3. passing an empty string should raise an error

Lastly we will explore using fixtures to parameterize our tests.
"""
import pytest


def backwards_allcaps(text):
    if len(text) == 0:
        raise AttributeError()
    return text[::-1].replace(' ', '').upper()


@pytest.fixture(params=[
    {'input': 'python', 'output': 'NOHTYP'},
    {'input': 'meetup', 'output': 'PUTEEM'},
    {'input': ' salt lake', 'output': 'EKALTLAS'},
])
def test_data(request):
    return request.param


def test_backwards_allcaps(test_data):
    assert backwards_allcaps(test_data['input']) == test_data['output']


def test_input_err():
    with pytest.raises(AttributeError):
        backwards_allcaps('')
