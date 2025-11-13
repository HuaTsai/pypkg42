"""Fibonacci Python Module"""

import time


def fib(n: int) -> int:
    """Compute the nth Fibonacci number using the recursive algorithm."""
    def _fib_recursive(n: int) -> int:
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        return _fib_recursive(n - 1) + _fib_recursive(n - 2)

    start_time = time.time()
    result = _fib_recursive(n)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"fib({n}) took {elapsed_time:.6f} seconds")

    return result
