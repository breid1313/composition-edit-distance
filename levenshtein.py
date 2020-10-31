import numpy as np

def levenshteinDP(object1, object2):
    # initilize the distance matrix
    m = object1.size
    n = object2.size
    distances = np.zeros((m + 1, n + 1), dtype=float)
    '''
    creates an initial matrix in the form of

    0 1 2 3 4 5 ... 
    1 0 0 0 0 0 ...
    2 0 0 0 0 0 ...
    3 0 0 0 0 0 ...
    4 0 0 0 0 0 ...
    5 0 0 0 0 0 ...
    ...............

    '''

    for i in range(m + 1):
        distances[i][0] = i
    for j in range(n + 1):
        distances[0][j] = j

    a = b = c = 0
    
    # calculate the distances between the prefixes
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if (object1[i-1] == object2[j-1]):
                distances[i][j] = distances[i - 1][j - 1]
            else:
                a = distances[i][j - 1]
                b = distances[i - 1][j]
                c = distances[i - 1][j - 1]

            if (a <= b and a <= c):
                distances[i][j] = a + 1
            elif (b <= a and b <= c):
                distances[i][j] = b + 1
            else:
                distances[i][j] = c + 1

    return distances[m][n]
