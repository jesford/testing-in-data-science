# contents of demo_pandas_hypothesis.py
from hypothesis import given
from hypothesis import strategies as st
from hypothesis.extra.pandas import data_frames, column
from scipy.special import expit  # logistic function


def probability_loyal_customer(df):
    "Return customer probability of returning."
    p_days_ago = df.days_since_last_order.apply(expit)
    p_num_orders = df.num_total_orders.apply(expit)
    p_loyal = p_days_ago * p_num_orders
    return p_loyal


@given(
    data_frames([
        column('days_since_last_order', dtype=int,
               elements=st.integers(min_value=0, max_value=365)),
        column('num_total_orders', dtype=int,
               elements=st.integers(min_value=0, max_value=1_000_000))])
)
def test_prob_loyality(df):
    p = probability_loyal_customer(df)
    assert p.between(0, 1, inclusive=True).all()
