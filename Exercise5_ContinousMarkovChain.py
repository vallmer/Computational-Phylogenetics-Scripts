"""
Created on Fri Apr 24 11:18:37 2015

@author: vallmerjordan
"""

"""
Exercise 5 - Creating a continuous-time Markov chain class
@author: jembrown
The point of this exercise is to define a new class, called ctmc (for continuous-
time Markov chain), that contains all necessary information and methods related
to such a chain, running simulations of these chains, calculating summaries of
chains, calculating probabilities of specific character histories, 
calculating marginal probabilities of starting and ending states, and estimating
branch lengths from the marginal probabilities using maximum likelihood.
This exercise is roughly divided into three steps:
(a) Define the ctmc class and its __init__ method. In the __init__, set up the
following variables associated with instances of ctmc:
- time (or branch length)
- state space (for our purposes this will usually be the 4 nucleotides)
- stationary (or equilibrium) frequencies of the states
- an 'R' vector defining the relative propensity for diff't changes
- a 'Q' matrix used to define rates of changes and calc. probabilities
- the number of simulations (or independent chains or sites)
- lists of event times generated by the simulations
- lists of event states generated by the simulations
- a list of starting states across simulations (optional - could also be the
  first element of the event states lists)
- a list of character history probabilities
- a list of marginal probabilities (using just starting and ending states,
  along with the branch length)
  
NOTES: In the usual method for defining GTR-class Q-matrices in phylogenetics,
the equilibrium frequencies and R-vector rates are used to define elements of
the Q-matrix. You can initialize them in any way you like, but it would be a 
good idea to write a function to make sure they are all consistent and to 
update elements of the Q-matrix when equil. frequencies or R-rates change.
  
(b) Define a method for simulating character histories using the Q-matrix.
Use these steps to simulate:
- Draw a starting state from the equilibrium frequencies
- Draw a waiting time from the appropriate exponential distribution
- Draw a new state from the marginal probabilities associated with the current
  state.
- Keep drawing waiting times and new states until the total time exceeds the
  branch length.
(c) Define a method that estimates branch lengths from marginal probabilities
using maximum likelihood. Use a 'site-independent' model, where the marginal
probability across the entire data set (i.e., across all simulations jointly)
is simply the product of the site probabilities.
"""

# We will need several functions from scipy
import scipy as sp
from __future__ import division
import random
import numpy as np

class ctmc(object):
    """         
    A class defining a continuous-time Markov chain (CTMC)
    """
          
    def __init__(self,
                 totalTime = 1.0,
                 States = ['A','C','G','T'],
                 equilFreqs = [0.25,0.25,0.25,0.25],
                 R = [4.0/3.0,4.0/3.0,4.0/3.0,4.0/3.0,4.0/3.0,4.0/3.0],
                 Q = np.array([[-1.0,(1.0/3.0),(1.0/3.0),(1.0/3.0)],
                      [(1.0/3.0),-1.0,(1.0/3.0),(1.0/3.0)],
                      [(1.0/3.0),(1.0/3.0),-1.0,(1.0/3.0)],
                      [(1.0/3.0),(1.0/3.0),(1.0/3.0),-1.0]])):
        self.totalTime = totalTime
        self.equilFreqs = equilFreqs
        self.R = R
        self.Q = Q
        self.margProbs = []
        self.exactProb = []
        self.P = sp.linalg.expm(sp.array(self.Q)*self.totalTime)
        
    def discSamp(self, events, probs):
        """
        This function samples from a list of discrete events provided in the events
        argument, using the event probabilities provided in the probs argument. 
        These lists must:
            - Be the same length
            - Be in corresponding orders
        Also, the probabilities in probs must sum to 1.
        """
        ranNum = sp.random.random()
        cumulProbs = []
        cumulProbs.extend([probs[0]])
        for i in range(1,len(probs)):
            cumulProbs.extend([probs[i]+cumulProbs[-1]])
        for i in range(0,len(probs)):
            if ranNum < cumulProbs[i]:
               return events[i]
        return None

    def Simulator(self):
        startRandom = self.discSamp(self, self.States, self.equilFreqs)
        stateSpace = startRandom[0]
        wait_time = 0
        accum_wait_time = 0
        stateList = []
        timeList = []
        while accum_wait_time <= self.total_time: # stops the chain when the branch length exeeds the sum of the times list
            # samples the waiting time from the exponential distribution using the appropriate value from the rateMatrix
            stateList.append(stateSpace)
            timeList.append(wait_time)
            wait_time = (random.expovariate(-(self.Q[self.States.index(stateSpace), self.States.index(stateSpace)])))
            accum_wait_time += wait_time
            current_probs = self.Q[self.States.index(stateSpace)] # takes the row from appropriate index from the stateSpace
            cpList = current_probs.tolist()
            cpList.pop(self.States.index(stateSpace))
            States_List = list(self.States)
            States_List.pop(self.States.index(stateSpace))
            next_state = self.discSamp(self, States_List, cpList)	
            stateSpace = next_state[0] #Reset the starting variable
        return stateList, timeList

"""    

# Simulate one site. Estimate branch length.


# Simulate several hundred sites. Estimate branch length.


# Run the above simulations repeatedly and examine variation in the estimated branch lengths.
