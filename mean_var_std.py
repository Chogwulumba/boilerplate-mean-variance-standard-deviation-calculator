import numpy as np

def calculate(list_9: list) -> dict:
    if len(list_9) < 9:
        raise ValueError("List must contain nine numbers.")
    matrix: np.ndarray = np.array(list_9)
    matrix: np.ndarray = matrix.reshape((3, 3))
    #print(np.hstack((matrix[0], matrix[1], matrix[2])))
    calculations = {'mean': [list(matrix.mean(axis=0)), list(matrix.mean(axis=1)), matrix.mean()],
    'variance': [list(matrix.var(axis=0)), list(matrix.mean(axis=1)), matrix.var()],
    'standard deviation': [list(matrix.std(axis=0)), list(matrix.std(axis=1)), matrix.std()],
    'max': [list(matrix.max(axis=0)), list(matrix.max(axis=1)), matrix.max()],
    'min': [list(matrix.min(axis=0)), list(matrix.min(axis=1)), matrix.min()],
    'sum': [list(matrix.sum(axis=0)), list(matrix.sum(axis=1)), matrix.sum()]}
    return calculations

print(calculate([i for i in range(0, 9)]))