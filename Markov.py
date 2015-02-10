"""
Exercise 4
Discrete-time Markov chains
@author: vallmerjordan

In this exercise, we will explore Markov chains that have discrete state spaces
and occur in discrete time steps. To set up a Markov chain, we first need to 
define the states that the chain can take over time, known as its state space.
To start, let's restrict ourselves to the case where our chain takes only two
states. We'll call them A and B.
"""

# Create a tuple that contains the names of the chain's states
# Definition:
# TUPLE- is an immutable list. A tuple can not be changed in any way once it is created.

Chain_States = ('A','B')

"""
The behavior of the chain with respect to these states will be determined by 
the probabilities of taking state A or B, given that the chain is currently in 
A and B. Remember that these are called conditional probabilities (e.g., the 
probability of going to B, given that the chain is currently in state A is 
P(B|A).)
We record all of these probabilities in a transition matrix. Each row
of the matrix records the conditional probabilities of moving to the other
states, given that we're in the state associated with that row. In our example
row 1 will be A and row 2 will be B. So, row 1, column 1 is P(A|A); row 1, 
column 2 is P(B|A); row 2, column 1 is P(A|B); and row 2, column 2 is P(B|B). 
All of the probabilities in a ROW need to sum to 1 (i.e., the total probability
associated with all possibilities for the next step must sum to 1, conditional
on the chain's current state).
In Python, we often store matrices as "lists of lists". So, one list will be 
the container for the whole matrix and each element of that list will be 
another list corresponding to a row, like this: mat = [[r1c1,r1c2],[r2c1,r2c2]]. 
We can then access individual elements use two indices in a row. For instance,
mat[0][0] would return r1c1. Using just one index returns the whole row, like
this: mat[0] would return [r1c1,r1c2].
Define a transition matrix for your chain below. For now, keep the probabilities
moderate (between 0.2 and 0.8).
"""

# Define a transition probability matrix for the chain with states A and B

r1c1 = float(input("Please insert value for P(A|A): ")) 
r1c2 = float(input("Please insert value for P(B|A): ")) 
r2c1 = float(input("Please insert value for P(A|B): "))
r2c2 = float(input("Please insert value for P(B|B): "))

p_Matrix = [[r1c1,r1c2],[r2c1,r2c2]]

# Try accessing a individual element or an individual row 

# Element

element = p_Matrix[0][0]

# Row

row = p_Matrix[0][0:2]

print element

print ' '

print row
"""
Now, write a function that simulates the behavior of this chain over n time
steps. To do this, you'll need to return to our earlier exercise on drawing 
values from a discrete distribution. You'll need to be able to draw a random
number between 0 and 1 (built in to scipy), then use your discrete sampling 
function to draw one of your states based on this random number.
"""

# Import scipy U(0,1) random number generator



# Paste or import your discrete sampling function

# Write your Markov chain simulator below. Record the states of your chain in 
# a list. Draw a random state to initiate the chain.

def Markov(steps):
   import scipy
   State_List= []
   RandNum = scipy.random.random()
   if RandNum <= .5:
       State = 'A'
   else:
       State = 'B'
   State_List.append(State)
   for s in range(steps):
       State = State
       if State=='A':
           x=scipy.random.random()
           if x<=r1c1:
               State = 'A'
               State_List.append(State)
           else:
               State = 'B'
               State_List.append(State)
       
       elif State == 'B':
           x=scipy.random.random()
           if x<=r1c2:
               State='A'
               State_List.append(State)
           else:
               State='B'
               State_List.append(State)
   print(State_List)
       
Markov(10)
