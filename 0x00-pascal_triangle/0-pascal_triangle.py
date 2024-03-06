def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []

    for height in range(n):
        row = [1]
        for i in range(1, height):
            row.append(triangle[height - 1][i - 1] + triangle[height - 1][i])
        if triangle != 0:
            row.append(1)
        triangle.append(row)
    return triangle
