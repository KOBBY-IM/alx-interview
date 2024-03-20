#!/usr/bin/python3
"""Minimum operations to achieve n H characters in a file."""


def minOperations(n):
    """
    Calculate the fewest number of operations needed to achieve exactly
    n H characters in the file.

    Args:
        n (int): The desired number of H characters.

    Returns:
        int: The minimum number of operations needed to achieve n H characters.
             If n is impossible to achieve, returns 0.
    """
    if n == 1:
        return 0  # Base case: Already one char is present

    # Initialize a list to store min operations needed
    # for each number of chars
    a = [float('inf')] * (n + 1)
    a[1] = 0  # Base case: No operations needed for one char

    # Iterate through each possible number of chars
    for i in range(2, n + 1):
        # Try all possible lengths of copied substring
        for j in range(1, i):
            # Check if the current length is a divisor of i
            if i % j == 0:
                # Update the min operations needed
                a[i] = min(a[i], a[j] + (i // j))

    # If the solution is found, return the min operations for n H chars
    # Otherwise, return 0 indicating it's impossible to achieve n chars
    return a[n] if a[n] != float('inf') else 0
