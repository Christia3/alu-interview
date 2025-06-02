#!/usr/bin/python3
"""
Module to generate Pascal's Triangle.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal’s triangle of n.

    Args:
        n (int): Number of rows in the triangle.

    Returns:
        List[List[int]]: Pascal's triangle represented as a list of lists.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # First row

    for i in range(1, n):
        prev_row = triangle[-1]
        row = [1]
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)
        triangle.append(row)

    return triangle

