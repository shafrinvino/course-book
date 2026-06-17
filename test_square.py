from square import square

def test_square():
    assert square(5) == 25

def test_square_zero():
    assert square(0) == 0

def test_square_negative():
    assert square(-4) == 16
