# -*- coding: utf-8 -*-
"""
This module provides a function that returns both minimum
and maximum element from a given sequence.  This is a part
of the exercises given under the course UIT2201 (Programming
and Data Structures).

This is a sample implementation and may contain bugs!
We have tried to follow good coding practices but don't
claim that this source code is perfect!

Your comments and suggestions are welcome.

Created on Wed Apr 05 2023

Revised on Wed Apr 07 2023

Original Author: C. Aravindan <AravindanC@ssn.edu.in>

$Id: 7b7120e18cfce7462a470e6866355e33bfdd495c $
"""
# Always leave TWO blank lines to separate "sections" of code


def minmax(aSeq):
    """ Finds and returns both the minimum and maximum objects
    from the given sequence.  The input sequence is expected to
    be ordered, meaning the indices for the elements are defined.
    Further, we assume that the sequence contains objects for which
    a partial order has been defined and can be compared using
    standard Python comparison operators.

    The input sequence may be empty, in which case 'None' is 
    returned.

    The input sequence is not modified and there are no side
    effects.

    aSeq: A sequece of indexed objects that can be compared.
    
    returns: A tuple of minimum and maximum objects in aSeq.
             'None' is returned if aSeq is empty.
    """
    seqSize = len(aSeq)
    if seqSize == 0:
        return None
    if seqSize == 1:
        return (aSeq[0], aSeq[0])
    if seqSize == 2:
        if aSeq[0] < aSeq[1]:
            return(aSeq[0], aSeq[1])
        else:
            return(aSeq[1], aSeq[0])
    else:
        current_min = current_max = aSeq[0]
        for index in range(1,seqSize):
            if aSeq[index] < current_min:
                current_min = aSeq[index]
            elif aSeq[index] > current_max:
                current_max = aSeq[index]
        return (current_min, current_max)
# End of function 'minmax'


# We will use the random module to generate an integer within
# a given range under uniform distribution
import random


def create_random_int_list(size=1000, low=-100000, high=100000):
    """ Create and return a list (of len 'size') containing random integers
    in the range from 'low' to 'high'.

    size:  Length of the desired random list
    low:  The lower end of the range of numbers
    high:  The higher end of the range of numbers

    returns: A new list of given size containing random integers
    """
    random_list = []
    for count in range(size):
        random_list.append(random.randint(low, high))
    return random_list
# End of function 'create_random_int_list'


# Let's add some code for testing
if __name__ == '__main__':
    # Following code will be executed only when this Python
    # file is run directly.  Code will be ignored if this
    # file is imported by another Python source.


    # Print some random lists to test the create_random_int_list function
    print(create_random_int_list(0))   # Expecting an empty list
    print(create_random_int_list(-10)) # Can 'size' be negative!?
    print(create_random_int_list(1))
#    print(create_random_int_list(10))
#    print(create_random_int_list(7, -10, 100))
#    print(create_random_int_list())


    testSeq = ()
    print(minmax(testSeq)) # 'None' should be returned
    testSeq = ["அரவிந்தன்"]
    print(minmax(testSeq)) # Both min and max are the only element
    testSeq = ["அரவிந்தன்", "அறவள்ளுவன்"]
    print(minmax(testSeq)) # Do we know Tamil sorting order!?
    testSeq = ["அரவிந்தன்", "அறவள்ளுவன்", "பாரதி", "ஔவையார்", "மணிமேகலை"]
    print(minmax(testSeq))
    print(minmax(minmax(testSeq))) # We reach the 'fixfoint' of our function!
    testSeq = ([1,2], [3,1], [2,1,7], [8], [])
    print(minmax(testSeq)) # Does this work!?
    testSeq = {2.12, 3.14, 0.314, -3.14, 1.11, -4.13, 3.145}
    print(minmax(list(testSeq))) # Note that our function does not work on sets!


    # Let's now test our function with some random lists.
    # When we test with large random lists, how do we know
    # that the answers returned are correct?
    num_trials = random.randint(10, 30)
    for trial in range(num_trials):
        trial_size = random.randint(0, 10)
        # Create a random list
        rList = create_random_int_list(trial_size, -1000000, 1000000)
#       print(rList)
        # Use our function to find min and max
        answer = minmax(rList)
        # Cross check with actual min and max
        if len(rList) == 0:
            right_answer = None
        else:
            right_answer = (min(rList), max(rList))
        print(answer, right_answer)
        if (answer != right_answer):
            raise Exception("Function 'minmax' has returned a wrong answer!")
