def fibonacci(n):
        """ Returns the nth number from the Fibonacci sequence.
            Example: fibonacci(0) == 1
            Example: fibonacci(1) == 1
        """
        a = 1
        b = 1

        if(n == 0):
            return a

        for i in range(n-1):
            (a, b) = (b, a + b)
        return b


def lucas(n):
        """ Returns the nth number from the Lucas Numbers sequence.
            Example: lucas_numbers(0) == 2
            Example: lucas_numbers(1) == 1
        """
        a = 2
        b = 1

        if(n == 0):
            return a

        for i in range(n-1):
            (a, b) = (b, a + b)
        return b


def sum_series(n, seed1=1, seed2=1):
        """ The required parameter determines which element in the series to print.
        """
        a = seed1
        b = seed2

        if(n == 0):
            return a

        for i in range(n-1):
            (a, b) = (b, a + b)
        return b


if __name__ == "__main__":
    # Test fibonacci
    assert(fibonacci(0) == 1)
    assert(fibonacci(1) == 1)
    assert(fibonacci(2) == 2)
    assert(fibonacci(3) == 3)
