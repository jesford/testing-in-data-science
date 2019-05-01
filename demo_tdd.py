import pytest


def backwards_allcaps(text):
    text = text.replace(' ', '')
    if len(text) == 0:
        raise AttributeError('String must contain letters')
    return text[::-1].upper()


@pytest.fixture(params=[
    {'input': 'python', 'output': 'NOHTYP'},
    {'input': 'meetup', 'output': 'PUTEEM'},
    {'input': 'salt lake', 'output': 'EKALTLAS'}])
def test_data(request):
    return request.param


def test_backwards_allcaps(test_data):
    assert backwards_allcaps(test_data['input']) == test_data['output']


def test_bad_string():
    with pytest.raises(AttributeError):
        backwards_allcaps('')
