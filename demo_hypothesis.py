# contents of hypothesis_examples.py
from hypothesis import given, example
from hypothesis import strategies as st


def backwards_allcaps(text):
    return text[::-1].upper()


@given(st.text())
def test_backwards_allcaps(input_string):
    modified = backwards_allcaps(input_string)
    assert input_string.upper() == ''.join(reversed(modified))
