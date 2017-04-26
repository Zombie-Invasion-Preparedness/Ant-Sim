import numpy as np

def initAntGrid(n, prob):
    antGrid = np.zeros((n+2, n+2))
    probGrid = np.random.random((n+2, n+2))
    for i in range(len(probGrid)):
        for j in range(len(probGrid[i])):
            if probGrid[i][j] > prob:
                antGrid[i][j] = 0
            else:
                antGrid[i][j] = np.random.randint(1, 4)
    return antGrid