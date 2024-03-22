#!/usr/bin/python3
"""
Mininum Operations
"""


def minOperations(n):
    """
    Calculates the minimum operations needed to reach n H characters
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while factor * factor <= n:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    if n > 1:
        operations += n

    return operations
