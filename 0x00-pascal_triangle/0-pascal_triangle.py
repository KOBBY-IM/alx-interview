#!/usr/bin/python3
""" pascals triangle"""


def pascal_triangle(n):
    """
    Generates a list of lists representing Pascal's triangle of size n.

    Args:
        n (int): The number of rows in the Pascal's triangle.

    Returns:
        list: A list of lists representing Pascal's triangle,
        where each inner list represents a row.
    """

    # Handle cases where n is invalid
    if n <= 0:
        return []  # Return an empty list for invalid n

    triangle = [[1]]  # Initialize the triangle with the first row [1]

    # Generate remaining rows iteratively
    for i in range(1, n):
        row = [1]  # Start each row with 1

        # Calculate the remaining elements in the current row
        for j in range(1, i):
            element = triangle[i - 1][j - 1] + triangle[i - 1][j]
            # Sum the elements above
            row.append(element)

        row.append(1)  # Append a 1 at the end of each row
        triangle.append(row)  # Add the completed row to the triangle

    return triangle
