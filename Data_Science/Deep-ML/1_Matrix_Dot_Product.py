def dot_product(matrix, vector):
    # Check if matrix is not empty and is a list of lists
    if not matrix or not isinstance(matrix[0], list):
        return -1

    # Number of columns in the matrix should match length of vector
    num_cols = len(matrix[0])
    if len(vector) != num_cols:
        return -1

    result = []
    for row in matrix:
        # Additional check: all rows must have the same number of columns
        if len(row) != num_cols:
            return -1
        dot = sum(r * v for r, v in zip(row, vector))
        result.append(dot)

    return result
