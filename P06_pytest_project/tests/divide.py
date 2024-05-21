## Calculator code ##
def divide(self, a, b):
    return a / b

## Pytest code ##
def test_divide(self):

    # arrange
    a = 20
    b = 4
    cal = Calculator()

    # act
    result = cal.divide(a,b)

    # assert
    expected = 5
    assert result == expected
    