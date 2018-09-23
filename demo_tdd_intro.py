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
def backwards_allcaps(text):
    return text[::-1].upper()


def test_backwards_allcaps():
    assert backwards_allcaps('python') == 'NOHTYP'
    assert backwards_allcaps('meetup') == 'PUTEEM'
