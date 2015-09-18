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


