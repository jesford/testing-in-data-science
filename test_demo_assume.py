from hypothesis import given, assume
from hypothesis import strategies as st
import numpy as np


@given(st.floats())
def test_double_negative(val):

    assert val == -(-val)
