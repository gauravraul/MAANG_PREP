def transpose(matrix):
    # Check if matrix is not empty
    if not matrix or not isinstance(matrix[0], list):
        return []

    # Transpose using zip and list comprehension
    return [list(row) for row in zip(*matrix)]
