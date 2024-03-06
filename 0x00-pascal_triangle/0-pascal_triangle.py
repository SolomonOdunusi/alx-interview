"""Pascal Triangle"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to a given number of rows (n).

    Args:
        n: The number of rows in the triangle.

    Returns:
        A list of lists representing the Pascal's triangle.
    """
    if n <= 0:
        return []
    triangle = []

    for height in range(n):
        row = [1]

        for i in range(1, height):
            row.append(triangle[height - 1][i - 1] + triangle[height - 1][i])

        if height > 0:
            row.append(1)

        triangle.append(row)

    return triangle
