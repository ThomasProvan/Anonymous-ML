# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 17:42:26 2018

@author: Der Niabs

ML System
    Helper Object for the protocol
    Provides access to the ML backend.
    One per ML System
    Minimal Parameters - We'll be pre-setting or auto-calculating parameters
    Basic functions:
        Train - Input: Data. No output. Parameters set by the helper. 
        Test - Input: Data. Output: Varies by system.
        
    Questions
        How simple do we want this to be? Could combine the comparator into
        this, but since the comparator is our ultimate output, we probably
        want it to be as consistent as possible.


"""
from sklearn.neighbors import NearestNeighbors
import numpy as np

class KNearestSystem:
    
    # Think about K settings. May want to bump it up higher.
    #   100 seems... okay? We've got a bit of an outlier problem in the current
    #   dataset. There are a few connections that dominate the traffic.
    # Still need to figure out statistical analysis as well.
    # May also want to enable multi-core. Looks like it should just be an init
    # option.
    
    # Update: getting interpretable results at 100, I think. May still want to
    # enable multi-core, and other datasets may produce better results at
    # different values.
    # Multi core added. It's so satisfying to watch my CPU max out
    
    # Consider adding a function to change parameters, or see if there's a principled
    # way to set K from a given dataset that we can use instead of manual setting.
    
    NUM_NEIGH = 100
    
    result_size = NUM_NEIGH * 2
    
    def __init__(self):
        # Init Garbage Here. Just reminding myself how python works
        # It's been way too long since I wrote code. Way too long.
        self.mlSys = NearestNeighbors(n_neighbors = self.NUM_NEIGH, n_jobs=-1)
        self.trained = False

    def train(self, data):
        self.mlSys.fit(data)
        self.trained = True
        
        
    def test(self, data):
        # No need to save this, we're just going to be outputting results.
        # Hmm... Right, KNN.
        # TODO: Output. Ideally we want this to be consistent, but KNN has very
        # different outputs to everything else we'll be looking at...
        if not self.trained:
            raise RuntimeError("ML System not trained before testing")
        dist, index = self.mlSys.kneighbors(data)
        return np.concatenate((dist, index), axis=1)
    
    # Cleans up result somewhat. May add more stuff here later, but right now
    # this is *mostly* to account for the weirdness of KNN and instance based
    # learners. But we want it here so that the controllers don't have to care
    # about that kind of crap.
    def cleanUp(self, result, train_index, test_index):
        for x in range(0,result.shape[0]):
            for y in range(self.NUM_NEIGH,self.NUM_NEIGH*2):
                index = int(result[x,y])
                result[x,y] = train_index[index]
        return result
    
"""
Okay, let's examine a question. Does this need to be a class?
Probably not, but my OO inclinations tell me to make it one XD

Let's see... oh, okay, I have an okay reason to do it this way.

We're going to be training 2 different machines with each type.
Comparing them is going to be relevant, so having a system object
for each run seems reasonable. We can then use other functions to
compare the two.

Hrm... Cross-fold. Where do / How do / Do we want to handle cross-fold?
We haven't answered that question quite yet. See TestController for more rambling
--- sk-learn has some cross-fold functions. Still need to hash out specifics

Secondary question: Do we want to have a MLSystem superclass?

I'm not sure. Just might not be relevant to make a superclass. It would be an
organizational tool, not a computational one. It would be useful in C++, in
Python I don't think it matters at all. There's no functions that I would want
to define at the level above this. Yay for weak typing?

On a completely unrelated note, weak typing makes me nervous sometimes XD

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