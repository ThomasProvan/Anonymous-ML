# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 17:42:26 2018

@author: Der Niabs
"""
from sklearn.neighbors import NearestNeighbors
import numpy as np

class KNearestSystem:
    
    
    
    def __init__(self):
        # Init Garbage Here. Just reminding myself how python works
        # It's been way too long since I wrote code. Way too long.




"""
KNN specific notes.

Here's some example code for running unsupervised KNN from scikit-learn

>>> from sklearn.neighbors import NearestNeighbors
>>> import numpy as np
>>> X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
>>> nbrs = NearestNeighbors(n_neighbors=2, algorithm='ball_tree').fit(X)
>>> distances, indices = nbrs.kneighbors(X)
>>> indices                                           
array([[0, 1],
       [1, 0],
       [2, 1],
       [3, 4],
       [4, 3],
       [5, 4]]...)
>>> distances
array([[ 0.        ,  1.        ],
       [ 0.        ,  1.        ],
       [ 0.        ,  1.41421356],
       [ 0.        ,  1.        ],
       [ 0.        ,  1.        ],
       [ 0.        ,  1.41421356]])

"""