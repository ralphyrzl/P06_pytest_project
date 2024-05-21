## Calculator code ##
def multiply(self, a, b):
    return a * b

## Pytest code ##
def test_multiply(self):

    # arrange
    a = 5
    b = 4
    cal = Calculator()

    # act
    result = cal.multiply(a,b)

    # assert
    expected = 20
    assert result == expected
    