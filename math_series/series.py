def fibonacci(n):
    """
    function to find values at a position in the Fibonacci Series
    :param n: the position in the fibonacci sequence
    :return: the value at that position in the sequence
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)

def lucas(n):
    """
    function to find values at a position in the Lucas Series
    :param n: the position in the series
    :return: the value at that position in the series
    """
    if n <= 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 2) + lucas(n - 1)

def sum_series(n, x = 0, y = 1):
    """
    function to determine value in series of either Fibonacci Series or Lucas series
    :param n: postion in the series to test
    :param x:(optional) if blank will test Fibonacci, if 2 will test Lucas
    :param y:(optional) if blank will test Fibonacci, if 1 will test Lucas
    :return: the value at that position in the series
    """
    if x == 0 and y == 1:
        return fibonacci(n)
    elif x == 2 and y == 1:
        return lucas(n)

# print(sum_series(8))
# print(sum_series(8,2,1))