# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 03:15:20 2018

@author: Der Niabs

Manages the execution of a single test. Takes in the data-structure and ML system,
then does necessary data anon & splitting and execution of the ML System. 
"""
import numpy as np
from sklearn.model_selection import KFold


class TestController:
    
    # data: un-anonymized data, in array-like format
    # dataAnon: anonymized, in the same order as data.
    #   May swap this out for an alg instead later. Uncertain where exactly
    #   we want to do the anonymization, but I'm thinking we want to do it before
    #   this stage.
    def __init__(self, data, dataAnon = None):
        self.data = np.array(data)
        self.dataAnon = dataAnon
        # Generates cross-fold indexes on command. Useable only once without
        # saving the indecies.
        # If we want to randomize the data order, do it elsewhere to maintain
        # the relationship between data and dataAnon.
        self.kf = KFold(n_splits = 10)

    # mlSys: one of our defined mlSystems. I may make a super class later, but
    # for now I'm just going to use some lazy typing. Because python.
    def run(self, mlSys):
        # Anonymization & cross-fold already done at this step.
        
        # Probably want to initialize this to the length of data, store results
        # by index.
        results = []
        
        # For each split
        for train_index, test_index in kf.split(data):
            train = self.data[train_index]
            test = self.data[test_index]
            mlSys.train(train)
            mlSys.test(test)
            


# Note on cross-fold: scikit-learn has some cross-fold validation helper functions


# Having thrashing problems figuring out the structure... ugh.
"""
Hmm... Okay, thought to fiddle with. What about one TestController that we
pass ML systems to run? 
    
Okay, I think I like this structure better the more I think about it... just
having a lot of thrashing problems lately.
"""

# Outline time

"""

Segments

    Test Protocol
        Running a full test of a ML system        
        Should be written once. 
        Input: Raw Data, TCPDump, Netflow, or either.
            Probably placing this into a data-structure before it hits this
            function, and passing it around that way.
            It is also possible that we'll be using a data-base for access.
            Depends on how much data we want to work with. There are limits
            to how much we can shove into Python at once.
        Input: ML system
        Output: Statistics
        Output: per dataum differences on ML output.
        1) Anonymization of Raw Data (possibly with multiple algs)
        2) Run the control: Train & Test on raw data.
            Inputs: Raw data
            Outputs: **Varies by system type**. Comparator class may be needed.
                KNN: Distance to neighbors, specific neighbors? To hammer out
                Anomaly: Anomaly value, 0-1, per dataum. Easy.
                Clustering: Cluster size & membership? To hammer.
            Use Cross-fold to generate information for each field.
        3) Run the tests: 3 conditions. Outputs should be the same as control.
        4) Comparison & Statistics
            Takes the outputs of all the tests, generates comparison statistics.
            
        Questions
            Cross-fold: split once, per protocol, or per test?
                If per test, should the ML system handle that?

        Performance dependent: How many ML systems we train in one execution

    ML System
        Helper Object for the protocol
        Provides access to the ML backend.
        One per ML System
        Basic functions:
            Train - Input: Data. No output. Parameters set by the helper. 
            Test - Input: Data. Output: Varies by system.
            
        Questions
            How simple do we want this to be? Could combine the comparator into
            this, but since the comparator is our ultimate output, we probably
            want it to be as consistent as possible.
            
    ML Comparator
        Helper Object for Protocol
        Compiles test results into statistics
        One per class of ML system (KNN, Anomaly, Clustering, ???)
            Should be much fewer of these.

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