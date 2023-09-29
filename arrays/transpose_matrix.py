def transposeMatrix(matrix):
    transposed_matrix=[]
    for items in zip(*matrix):
        transposed_matrix.append(list(items))

    return transposed_matrix
