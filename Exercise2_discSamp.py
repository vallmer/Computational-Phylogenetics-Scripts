"""
Created on Wed Feb 18 15:44:45 2015

@author: vallmerjordan
"""

"""
(1) Write a function that multiplies all consecutively decreasing numbers 
between a maximum and a minimum supplied as arguments. (Like a factorial, but not
necessarily going all the way up to 1). 

def psuFact(minimum,maximum): #Define function takes two numbers as input (min,max)
    m = maximum # store max value in variable outside of loop
    for i in range(1,maximum): create loop to multiple all numbers within the specified range
        z = m - i 
        if z >= minimum:
            maximum = maximum * z
        else: quit
    return maximum
"""

"""
(2) Using the function you wrote in (1), write a function that calculates the binomial 
coeffiecient (see Definition 1.4.12 in the probablility reading). Actually, do this 
twice. The first (2a) calculate all factorials fully. 

def biCF(n,k):
    bfNum = psuFact(1,n)
    bfDen = psuFact(1,(n-k))*psuFact(1,k)
    binCoA = bfNum/bfDen
    return binCoA


"""
"""
(2b)Now re-write the function and cancel as many terms as possible so you can 
avoid unnecessary multiplication (see the middle expression in Theorem 1.4.13).

def binCo(n,k):
    return psuFact((n-k+1),n) / psuFact(1,k)
"""
"""
(3) Try calculating different binomial coefficients using both the functions from
(2a) and (2b) for different values of n and k. Try some really big value there is 
a noticeable difference in speed between the (2a) and (2b) function. Which one is
faster? By roughly how much?


import time    
def bc_Comp(n,k): # Define function that compares speed between both binomial coefficient functions (2a,2b)
    start1 = time.time() # Store start time in variable start1
    biCF(n,k) # Compute the binomial coefficient using the first function
    end1 = time.time() #Store the end time in variable end1
    time1 = end1-start1 #Store total elapsed time in variable time1
    
    start2 = time.time() #Store start time for second function in variable start2
    bino = binCo(n,k) # Compute the binomial coefficient using the second function
    end2 = time.time() #Store end time for second function in variable start2
    time2 = end2-start2 #Store total elapsed time in variable time2
    
    # Print elapsed time for each function to the screen. Determine which is faster 
    # and by much. Then print that information to the screen

    A1 = time2 - time1
    A2 = time1 - time2

    print ''
    print 'The binomial coefficient: ', bino
    print ''
    print 'The total elapsed time (2A): ', time1
    print ''
    print 'The total elapsed time (2B): ', time2
    print ''

    if time1 < time2:
        print 'The equation in 2a computed the binomial coefficient ',
        print A1, ' seconds faster than the equation used in 2b'
    elif time1 == time2:
        print 'Equations in 2a and 2b took the same amount of time to' 
        print 'compute the binomial coefficient'
    else:
        print 'The equation in 2b computed the binomial coefficient ',
        print A2, ' seconds faster than the equation used in 2a'
"""
"""
(4) Use either function (2a) or (2b) to write a function that calculates the probability of 
k successes in n Bernoulli trials with probability p. This is called the Binomial(n,p)
distribution. See Theorem 3.3.5 for the necessary equation. [Hint: pow(x,y) returns x^y 
(x raised to the power of y).]

def binPMF(p,n,k):
    return int(binCo(n,k))*pow(p,k)*pow((1-p),(n-k))
"""
"""
(5) Now write a function to sample from an arbitrary discrete distribution. This function
should take two arguments. The first is a list of arbitrarily labeled events and the second
is a list of probabilities associated with these events. Obviously, these two lists should
be the same length.
"""
import scipy
from scipy import stats
#Prompt user to input event list, prob list, and # of sites
for i in range(100): # Loop to make sure len(events) = len(probs). 100 chances should be enough
    events= eval(raw_input('Please insert your list of events: '))
    probs = eval(raw_input('Please insert your list of probabilities for each event: '))
    sites = eval(raw_input('Please insert the total number of sites: '))
    if len(events) == len(probs) and sum(probs) == 1:
        break
    else: print '\nError: len(events) != len(probs)','\n       and/or sum(probs) != 1'       
# define Samp function. Construct an arbitrary distribution using the event list, prob list, and # of sites.
def Samp(events,probs,sites):
    sp = scipy.stats.rv_discrete(values=(events,probs))
    return sp.rvs(size=sites)
def discSamp(sampsz): #Define function that will generate a predetermined number of samples from an arbitrary discrete distribution
    event1 = [] #Create an empty list to store occurences of event 1
    event2 = [] #Create an empty list to store occurences of event 2
    probslist = [] #Create an empty list to store probabilities from each sample
    
    for i in range(sampsz): # Create for loop to generate desired number of samples
        rand = Samp(events,probs,sites) #Store random sample in variable rand
        randlist= [] #Create an empty list to store values in variable rand
        for all in rand: #Append each rand value into randlist
            randlist.append(all)
        event1.append(randlist.count(0)) #Count occurences of event 1 in random sample, append to list event1
        event2.append(randlist.count(1)) #Count occurences of event 2 in random sample, append to list event2
        probslist.append((float(event1[i]))/((float(event1[i]))+(float(event2[i])))) #Determine the percentage of sites in which event1 was sampled then append to list
    discSamp.event1 = event1 #Store as subfunction to be accessed outside
    discSamp.event2 = event2 #Store as subfunction to be accessed outside
    discSamp.probslist = probslist #Store as subfunction to be accessed outside
    return event1, event2, probslist #Return all three lists
Samp(events,probs,sites)    
discSamp(100)
"""
(6) For an alignment of 400 sites, with 200 sites of type 1 and 200 of type 2, sample a new
alignment (a new set of site pattern counts) with replacement from the original using your 
function from (5). Print out the counts of the two types.
"""
import scipy
from scipy import stats

Samp([0,1],[.5,.5],400)
discSamp(1)


"""
(7) Repeat (6) 100 times and store the results in a list.
"""
import scipy
from scipy import stats

Samp([0,1],[.5,.5],400)
discSamp(100)

"""
(8) Of those 100 trials, summarize how often you saw particular proportions of type 1 vs. type 2.

"""
#Plot discsamp data
import matplotlib.pyplot as plt   
def pltdiscSamp(successes):
    successTracker = []
    for k in successes:
        v = successes.count(k)
        successTracker.append('%s : %d' % (k, v))
    a = list(set(successTracker))
    xvalist = []
    yvalist = []
    for x in a:
        xval = x[0:3]
        xvalist.append(float(xval))
    pltdiscSamp.xval = xvalist
    for y in a:
        yval = y[6:]
        yvalist.append(float(yval))    
    yum = sum(yvalist)
    yperc_list = []
    for v in yvalist:
        yperc_list.append(v/yum)
    pltdiscSamp.yperc = yperc_list
    plt.ion
    plt.plot(xvalist,yperc_list,'ro')
    plt.axis([170,240,0,.08])
    plt.show()
    
pltdiscSamp(discSamp.event1)
"""
(9) Calculate the probabilities of the proportions you saw in (8) using the binomial
probability mass function (PMF) from (4).
"""
#Plot pmf data
def pmfPlot(successes):
    pmfList = []
    for e in pltdiscSamp.xval:
        pmfList.append(binPMF(.5,400,int(e)))
    pmfPlot.pmflist = pmfList
    plt.ion
    plt.plot(pltdiscSamp.xval,pmfList,'ro')
    plt.axis([170,240,0,.08])
    plt.show()
    
"""
(10) Compare your results from (8) and (9).
"""
plt.ion
plt.plot()
plt.plot(pltdiscSamp.xval,pmfList,'ro', pltdiscSamp.xval,pltdiscSamp.yperc,'bs')
plt.axis([170,240,0,.08])
plt.show()
"""
(11) Repeat 7-10, but use 10,000 trials.
"""
Samp([1,2],[.5,.5],400)
discSamp(10000)
pltdiscSamp(discSamp.event1)
pmfPlot(pltdiscSamp.xval)

plt.ion
plt.plot()
plt.plot(pltdiscSamp.xval,pmfPlot.pmflist,'ro', pltdiscSamp.xval,pltdiscSamp.yperc,'bs')
plt.axis([170,240,0,.08])
plt.show()
