import numpy as np

# originalPoints = np.array([[0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 1], [0, 5, 1, 0, 0, 0], [0, 0, 0, 0, 5, 1], [4, 5, 1, 0, 0, 0], [0, 0, 0, 4, 5, 1]])
# opInv = np.linalg.inv(originalPoints)

# mappedPointsStr = input("Enter 6 points separated by spaces")
# mappedPoints = np.asarray([ float(str) for str in mappedPointsStr.split(" ") ]).T

# solutions = opInv @ mappedPoints
# finalMat = np.reshape(solutions, (2, 3), order='C')
# finalMat = np.vstack((finalMat, np.array([0, 0, 1])))
# print(finalMat)

# Using sk image instead (can perform projective mappings as well)
from skimage import transform as tf

src = np.array([[0, 0, 4, 4, 1, 1, 3, 3, 1, 1, 0],
                [0, 5, 5, 4, 4, 3, 3, 2, 2, 0, 0]], float)

dst = np.array([[9.812, 10.1963302752294, 14.1855010660981, 13.4, 10.8298217179903, 10.6398305084746, 12.0611940298507, 11.7371879106439, 10.4931163954944, 10.2813455657492, 9.812], 
                [5.649, 8.39266055045871, 7.79957356076759, 6.91607142857143, 7.39059967585089, 6.74435028248588, 6.44328358208955, 5.95532194480946, 6.24530663329161, 5.5249745158002, 5.649]])

transform = tf.estimate_transform('projective', src.T, dst.T)
print(transform)