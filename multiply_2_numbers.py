
def multiply_numbers(num1, num2):
    """
    This function multiplies two numbers to each other.
    
    Parameters:
    num1 (int/float): The first number to be multiplied. It could be either an integer or a float.
    num2 (int/float): The second number to be multiplied. It could also be either an integer or a float.

    Returns:
    int/float: The product of num1 and num2. The return type will be float if either num1 or num2 was a float, otherwise it will be an integer.

    Examples:
    >>> multiply_numbers(2, 3)
    6
    >>> multiply_numbers(2.5, 4)
    10.0
    >>> multiply_numbers(-2, 3)
    -6
    >>> multiply_numbers(0, 100)
    0

    Edge Cases:
    >>> multiply_numbers(0, 0)
    0
    >>> multiply_numbers(float('inf'), 0)
    NAN
    >>> multiply_numbers(float('inf'), float('inf'))
    INF

    Note that the function does not handle the case when either num1 or num2 is not a number (either an integer or a float). 
    In such a case, the behavior of the function is not defined.
    """
    return num1 * num2


import unittest

class TestMultiplyNumbers(unittest.TestCase):

    def test_multiply_numbers(self):
        # Test basic functionality
        self.assertEqual(multiply_numbers(2, 3), 6)
        self.assertEqual(multiply_numbers(2.5, 4), 10.0)
        self.assertEqual(multiply_numbers(-2, 3), -6)
        self.assertEqual(multiply_numbers(0, 100), 0)

        # Test edge cases
        self.assertEqual(multiply_numbers(0, 0), 0)

        # python behavior for multiply of infinity with zero = nan
        self.assertTrue(isnan(multiply_numbers(float('inf'), 0)))
        # python behavior for multiply of infinity with infinity = infinity 
        self.assertTrue(isinf(multiply_numbers(float('inf'), float('inf'))))

        # Test error cases
        with self.assertRaises(TypeError):
            multiply_numbers("2", 3)
        with self.assertRaises(TypeError):
            multiply_numbers(2, "3")

if __name__ == '__main__':
    unittest.main()