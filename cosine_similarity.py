from numpy import dot
from numpy.linalg import norm

def cosineSimilarity(array1, array2):
    cosSim = dot(array1,array2) / (norm(array1)*norm(array2))
    print(cosSim)

cosineSimilarity(array1=[145,140,122],array2=[208.36, 149.32, 111.2])