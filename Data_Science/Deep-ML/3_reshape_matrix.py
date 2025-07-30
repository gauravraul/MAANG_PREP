def reshape_matrix(matrix, new_shape):
    # Flatten the original matrix
    flat = [item for row in matrix for item in row]
    
    # Check if total elements match the product of new shape dimensions
    total_elements = len(flat)
    rows, cols = new_shape
    if total_elements != rows * cols:
        return []

    # Build the reshaped matrix
    reshaped = [flat[i * cols:(i + 1) * cols] for i in range(rows)]
    return reshaped
