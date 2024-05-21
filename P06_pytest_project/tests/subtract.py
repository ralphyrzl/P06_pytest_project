## Calculator code ##
def subtract(self, a, b):
    return a - b

## Pytest code ##
def test_subtract(self):
    
    # arrange
    a = 4321
    b = 1234
    cal = Calculator()

    # act
    result = cal.subtract(a,b)

    # assert
    expected = 3087
    assert result == expected
