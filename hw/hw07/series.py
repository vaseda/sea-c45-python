
def fibonacci(n):
        """ Returns the nth number from the Fibonacci sequence.

            Keyword arguments:
            n -- number of the element in the series to calculate.

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

            Keyword arguments:
            n -- number of the element in the series to calculate.

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
        """ Returns the nth number of the sum_series.
        
            Keyword arguments:
            n -- number of the element in the series to calculate.
            seed1 -- first element of the series (default 1).
            seed2 -- second element of the series (default 2).
        """
        a = seed1
        b = seed2

        if(n == 0):
            return a

        for i in range(n-1):
            (a, b) = (b, a + b)
        return b
print sum_series(3)


if __name__ == "__main__":

    # Test fibonacci()
    assert(fibonacci(0) == 1)
    assert(fibonacci(1) == 1)
    assert(fibonacci(2) == 2)
    assert(fibonacci(3) == 3)
    # Test lucas()
    assert(lucas(0) == 2)
    assert(lucas(1) == 1)
    assert(lucas(2) == 3)
    assert(lucas(3) == 4)
    # Test sum_series() for fibonacci
    assert(sum_series(0, 1, 1) == 1)
    assert(sum_series(1, seed2=1, seed1=1) == 1)
    assert(sum_series(2) == 2)
    assert(sum_series(3) == 3)
    # Test sum_series() for lucas
    assert(sum_series(0, 2, 1) == 2)
    assert(sum_series(1, seed2=1, seed1=1) == 1)
    assert(sum_series(2, 2, 1) == 3)
    assert(sum_series(3, 2, 1) == 4)
