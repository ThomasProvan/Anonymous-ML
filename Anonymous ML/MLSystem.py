# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 18:29:03 2018

@author: Der Niabs

ML System
    Helper Object for the protocol
    Provides access to the ML backend.
    One per ML System
    Minimal Parameters - We'll be pre-setting or auto-calculating parameters
    Basic functions:
        init / constructor -- No input, should initialize the ML system for this
                                object and set any parameters for it.
        train -     Input: Data, in an NP array.
                    No output. Parameters set by the constructor.
        test -      Input: Data, in an NP array.
                    Output: Varies by system, but should be the results of running
                        the provided data through the ML system.
        cleanup -   Input: a 'result', from the test function
                    Input: Currently, the index mappings from cross-fold
                    Thus function 'cleansup' any side effects with the results
                        that are caused by the cross-folding system. Currently,
                        this is only necessary with K-Nearest, because it returns
                        indecies.
                    
        
    Questions
        How simple do we want this to be? Could combine the comparator into
        this, but since the comparator is our ultimate output, we probably
        want it to be as consistent as possible.


    This file should be used like a template, because Python doesn't like the
    idea of an abstract class very much, and there are no good 'default' values
    for these functions (except for cleanup). To make a new MLSystem, just copy
    this file and rename the class.
"""
import numpy as np

class MLSystem:
    
  
    # Size of the result returned by test for a single datapoint. Will vary per
    # ML system, but we need this value mostly because we're using NP arrays,
    # which behave similarly to C arrays.
    # TODO: Convert this to a function that takes in (data) as an input.
    # The classifiers have a variable-size output, based on the # of labels
    result_size = None
    
    # Constructor should set basic parameters for the ML system, and not
    # require any input.
    def __init__(self):
        self.trained = False

    """
    # Trains the ML system on new data. Should reset the current system to base
    # parameters
    """
    def train(self, data):
        self.trained = True
      
    """
    Tests the ML system on provided data. Should return the results of the
    classifier / anomaly detection / confidence / distance metric / whatever
    for each instance. Cannot be run before test. (Should probably write something
    to error out before it gets too far in that process)
    Must return a matrix of shape (data.shape[0], result_size)
    """
    def test(self, data):
        if not self.trained:
            raise RuntimeError("ML System not trained before testing")
        return None
    
    """
    Cleans up result, somewhat. May add more stuff here later, but right now
    this is *mostly* to account for the weirdness of KNN and instance based
    learners. But we want it here so that the controllers don't have to care
    about that kind of crap, and if other system specific oddities arise with
    returning results, we can handle them here.
    """
    def cleanUp(self, result, train_index, test_index):
        return result