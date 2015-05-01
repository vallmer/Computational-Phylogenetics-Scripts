"""
@author: vallmerjordan
"""

"""
Exercise 4
Discrete-time Markov chains
"""

# Create a tuple that contains the names of the chain's states

states = ("A","B") # Store the two chain states in a tuple named states

# Define a transition probability matrix for the chain with states A and B

tPm = [[0.6,0.4],[0.8,0.2]] #Create a transition probability matrix (two lists w/in list)

# Explore tPm

print(tPm[0][0]) #print first element in first list. Prob of A|A 

print(tPm[1]) #print elements in row 2. [P(A|B),P(B|B)]

"""
Now, write a function that simulates the behavior of a discrete-time Markov chain
"""

"""Chain Simulator"""

import scipy # to use scipy.random.random() for random number generator

# Paste discSamp function (key)
def discSampkey(events,probs):
    rand = scipy.random.random() # Generate random number
    cumProb = [] # create empty list for cumulative probabilities
    cumProb.extend([probs[0]]) # append probability for first event into cumProb
    for i in range(1,len(probs)): # Create a for loop to append cumulative probability (probability of event[i] + most recently appended probability in cumProb)
        cumProb.extend([probs[i]+cumProb[-1]])
    for i in range(0,len(probs)): # Create for loop that iterates through cumProb list using random numbers between 0 and 1 to simulate sampling
        if rand < cumProb[i]: # if cumProb is greater that random number (between 0 and 1)
            return events[i] # return that event
    return None

# Define discrete-time Markov chain function

def dmcSim(steps,state_space,Prob_matrix): # function requires number of steps, possible chain states, and corresponding transisiton probability matrix
    
    chain = [] # Create an empty list to store states simulated during each step 

    # Start chain with random state (each state has an equal probability of being initial state (1/n_of_state_spaces))    
    currState = discSampkey(state_space,[1.0/len(state_space) for x in state_space])
    chain.extend(currState) #Append randomly generated initial state to chain state list

    for step in range(1,steps): #Create for loop to simulate the remaining steps
        probs = Prob_matrix[state_space.index(currState)] # Store probability list of changing state given previous state in variable probs
        currState = discSampkey(state_space,probs) # simulate current state given probability assigned in line above to variable probs
        chain.extend(currState) # Add simulated state to chain list   
        
    return chain

simulate_10_steps = dmcSim(10,states,tPm) # simulate discrete-time Markov chain (10 steps)
print(simulate_10_steps) # print simulated output

#How often does the chain end in each state? How does this change as you change the transition matrix?
"""100 simulations---each with 100 steps"""

simulate_100dmc =[] #Create empty list to store output from each simulation

for i in range(100):
    simulate_100dmc.append(dmcSim(100,states,tPm))

Acount = 0
Bcount = 0

for i in range(100):
    if simulate_100dmc[i][-1] == "A":
        Acount += 1
    if simulate_100dmc[i][-1] == "B":
        Bcount += 1

print("Frequency of A: "+str(float(Acount)/100.0))
print("Frequency of B: "+str(float(Bcount)/100.0))

# Try defining a state space for nucleotides: A, C, G, and T. Now define a 
# transition matrix with equal probabilities of change between states.

states = ("A","C","G","T")

tPm = [[0.25,0.25,0.25,0.25],
         [0.25,0.25,0.25,0.25],
         [0.25,0.25,0.25,0.25],
         [0.25,0.25,0.25,0.25]]
         
# Again, run 100 simulations of 100 steps and look at the ending states. Then
# try changing the transition matrix.

"""         
tPm = [[0.35,0.15,0.20,0.30],
         [0.25,0.25,0.25,0.25],
         [0.05,0.45,0.25,0.25],
         [0.09,0.51,0.25,0.15]]
"""
      
nuc_sim = []

for i in range(100):
    nuc_sim.append(dmcSim(100,states,tPm))

nCnt = [0,0,0,0]

for i in range(100):
    if nuc_sim[i][-1] == "A":
        nCnt[0] += 1
    elif nuc_sim[i][-1] == "C":
        nCnt[1] += 1
    elif nuc_sim[i][-1] == "G":
        nCnt[2] += 1
    else:
        nCnt[3] += 1
        
print("Frequency of A: "+str(float(nCnt[0])/100.0))
print("Frequency of C: "+str(float(nCnt[1])/100.0))
print("Frequency of G: "+str(float(nCnt[2])/100.0))
print("Frequency of T: "+str(float(nCnt[3])/100.0))
