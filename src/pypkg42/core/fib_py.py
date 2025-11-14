"""Fibonacci Python Module"""


def fib(n: int) -> int:
    """Compute the nth Fibonacci number using the recursive algorithm."""
    if n <= 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    a, b = 1, 1
    for _ in range(2, n):
        a, b = b, a + b
    return b
