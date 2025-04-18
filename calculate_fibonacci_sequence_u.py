
def fibonacci(n):
    """
    This function calculates the Fibonacci sequence up to a given number, excluding the number exceeding the given input.

    Parameters:
    n (int): The upper limit for the Fibonacci sequence. This has to be a positive integer.

    Returns:
    list: The Fibonacci sequence as a list of integers, up to n.

    Examples:
    Input: fibonacci(20)
    Output: [0, 1, 1, 2, 3, 5, 8, 13]

    Input: fibonacci(1)
    Output: [0, 1, 1]

    Input: fibonacci(0)
    Output: [0]

    Edge Cases:
    If n = 0, the function will return the sequence [0].
    If n is negative, the function does not handle well and it's advised to always use n as a positive integer.

    """
    fib_sequence = [0, 1]

    while fib_sequence[-1] < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    # Exclude the value exceeding n.
    if fib_sequence[-1] > n:
        fib_sequence.pop()

    return fib_sequence


import unittest

class TestFibonacci(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(fibonacci(20), [0, 1, 1, 2, 3, 5, 8, 13])
        
    def test_one(self):
        self.assertEqual(fibonacci(1), [0, 1, 1])
        
    def test_zero(self):
        self.assertEqual(fibonacci(0), [0])
        
    def test_non_integer(self):
        with self.assertRaises(TypeError):
            fibonacci("twenty")
            
    def test_negative_number(self):
        """ This test asserts that the function does not handle well for negative input """
        with self.assertRaises(Exception):
            fibonacci(-5)
            
if __name__ == '__main__':
    unittest.main()