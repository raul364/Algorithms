from numpy.linalg import norm
import numpy as np
def euclidean(array1,array2):
    temp = array1-array2
    sumSQ = np.dot(temp.T,temp)
    print(np.sqrt(sumSQ))

euclidean(np.array((0,0)),np.array((10,10)))