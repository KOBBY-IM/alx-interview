#!/usr/bin/python3
""" minimum operations"""


def minOperations(n):
    """
    Calculate the fewest number of operations
    needed to result in exactly n H characters in the file.

    Args:
    - n: An integer representing the desired number of H characters

    Returns:
    - An integer representing the fewest number of operations
    needed to achieve n H characters
    - If n is impossible to achieve, returns 0
    """

    # Check if n is less than or equal to 1
    if a <= 1:
        return 0

    # Initialize the variable to count the number of operations needed
    op = 0
    # Start with the smallest prime divisor
    div = 2

    # Iterate until n is reduced to 1
    while a > 1:
        # If the current divisor divides n, repeatedly divide n by that divisor
        while a % div == 0:
            op += div
            a //= div

        # Move to the next divisor
        div += 1

    return op
