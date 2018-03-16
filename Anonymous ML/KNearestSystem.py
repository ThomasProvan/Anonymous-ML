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


    def train(data):
        self.input = data
        
        
        
    def test(data):
        # No need to save this, we're just going to be outputting results.

"""

Okay, let's examine a question. Does this need to be a class?
Probably not, but my OO inclinations tell me to make it one XD

Let's see... oh, okay, I have an okay reason to do it this way.

We're going to be training 2 different machines with each type.
Comparing them is going to be relevant, so having a system object
for each run seems reasonable. We can then use other functions to
compare the two.

Hrm... Cross-fold. Where do / How do / Do we want to handle cross-fold?
We haven't answered that question quite yet. Not sure how important that
is yet, we can implement later.


Secondary question: Do we want to have a MLSystem superclass?

I'm not sure. We can compare all the anomaly system with each other.
And if we had classes, then we could 
But ultimately we're evaluating how these systems behave within themselves.

"""


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