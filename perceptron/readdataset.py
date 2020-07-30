def read():
  return [
    [0, 0, 0],
    [0, 1, 0],
    [1, 0, 0],
    [1, 1, 1],
  ]

# generate data
# list of points 
import numpy as np 
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
np.random.seed(2)

means = [[2, 2], [4, 2]]
cov = [[.3, .2], [.2, .3]]
N = 10
X0 = np.random.multivariate_normal(means[0], cov, N).T
X1 = np.random.multivariate_normal(means[1], cov, N).T

X = np.concatenate((X0, X1), axis = 1)
print(X)
y = np.concatenate((np.ones((1, N)), -1*np.ones((1, N))), axis = 1)
# Xbar 
X = np.concatenate((np.ones((1, 2*N)), X), axis = 0)



import numpy as np 
import matplotlib.pyplot as plt
x, y = np.random.default_rng().multivariate_normal(means[0], cov, 5000).T
plt.plot(x, y, 'x')
x1, y1 = np.random.default_rng().multivariate_normal(means[1], cov, 5000).T
plt.plot(x1, y1, 'y')
plt.axis('equal')
plt.show()