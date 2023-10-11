#!/usr/bin/python3
"""
    This module prints the pascal triangle
"""


def pascal_triangle(n):
    """
        prints pascal triangle

        Args:
            n (int): number of rows
    """
    triangle = []
    num = 0
    while n > 0:
        row = []
        for i in range(num + 1):
            if i == 0 or i == num:
                row.append(1)
            elif num > 1:
                row.append(triangle[num - 1][i - 1] + triangle[num - 1][i])
        triangle.append(row)
        num += 1
        n -= 1
    return triangle
