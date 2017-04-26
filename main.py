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

def initPherGrid(n):
    pherGrid = [[0.0 for i in range(n)] for j in range(n)]
    pherGrid = numpy.array(pherGrid)
    pherGrid[n/2,:,] = 1.00
    pherGrid[:,0]= -0.01
    pherGrid[n - 1:,] = -0.01
    pherGrid[0,:]= -0.01
    pherGrid[n - 1:,] = -0.01
    pherGrid[:,n - 1] = -0.01
    return pherGrid