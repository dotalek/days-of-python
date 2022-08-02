"""Different implementations to solve for a given digit of the Fibonacci sequence."""


def fibonacci(n: int) -> int:
    """
    Recursively solves up to the given digit of the sequence.

    This solution has a time complexity of O(2**n).

        Parameters:
            n (int): Target digit in the sequence.

        Raises:
            RecursionError: if too many calls are made.

        Returns:
            (int): The calculated digit.
    """
    try:
        if n in [1, 2]:
            return 1
        return fibonacci(n - 1) + fibonacci(n - 2)
    except RecursionError as e:
        print("Unable to calculate digit, it's too far along the sequence.", e)
        return 0


def memo_fib(n: int, memo: dict[int, int] = {}) -> int:
    """
    Recursively solves up to the given digit of the sequence; using memoization.

    This solution has a time complexity of O(n).

        Parameters:
            n (int): Target digit in the sequence.
            memo (dict[int, int]): Stores previous results.

        Raises:
            RecursionError: if too many calls are made.

        Return
            (int): The calculated digit.
    """
    try:
        if n in memo:
            return memo[n]
        if n in [1, 2]:
            return 1
        memo[n] = memo_fib(n - 1, memo) + memo_fib(n - 2, memo)
        return memo[n]
    except RecursionError as e:
        print("Unable to calculate digit, it's too far along the sequence.", e)
        return 0


def bottom_fib(n: int) -> int:
    """
    Iteratively solves up to the given digit of the sequence; using a bottom-up approach.

    This soltion has a time complexity of O(n).

        Parameters:
            n (int): Target digit in the sequence.

        Return:
            (int): The calculated digit.
    """
    if n in [1, 2]:
        return 1
    fib = [1, 1] + [0] * (n - 2)
    for i in range(2, n):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n - 1]
