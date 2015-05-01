"""
An Introduction to Likelihood
@author: jembrown
"""

"""
There are two primary ways to use probability models. Given what we know to be true about an experimental setup,
 we can make predictions about what we expect to see in an upcoming trial. For this purpose, probability functions
 are what we need. If R is the outcome of an experiment (i.e., an event) and p is a parameter of the probability 
 function defined for these experimental outcomes, we can write these expectations or predictions as:
P(R|p).
This conditional probability tells us what to expect about the outcomes of our experiment, given knowledge of the 
underlying probability model. Thus, it is a probability function of R given a value for p (and the model itself).
However, we might also wish to ask what we can learn about p itself, given outcomes of trials that have already 
been observed. This is the purview of the likelihood. Likelihoods are functions of parameters (or hypotheses, more 
generally) given some observations. The likelihood function of a parameter value is defined as:
L(p;R) = P(R|p)
Note that this is the same probability statement we saw above. However, in this context we are considering the 
outcome (R) to be fixed and we're interested in learning about p. Note that the likelihood is sometimes written in 
several different ways: L(p;R) or L(p) or L(p|R). P(R|p) gives a probability when R is discrete or a probability 
density when R is continuous. Since likelihoods are only compared for some particular R, we do not need to worry 
about this distinction. Technically speaking, likelihoods are just said to be proportional to P(R|p), with the 
constant of proportionality being arbitrary.
There are some very important distinctions between likelihoods and probabilities. First, likelihoods do NOT sum 
(or integrate) to 1 over all possible values of p. Therefore, the area under a likelihood curve is not meaningful, 
as it is for probability.
It does not make sense to compare likelihoods across different R. For instance, smaller numbers of observations 
generally produce higher values of P(R|p), because there are fewer total outcomes.
Likelihood curves provide useful information about different possible values of p. When we are interested in 
comparing discrete hypotheses instead of continuous parameters, the likelihood ratio is often used:
L(H1;R)     P(R|H1)
-------  =  -------
L(H2;R)     P(R|H2)
Now, let's try using likelihoods to learn about unknown aspects of the process that's producing some data.
---> Inferring p for a binomial distribution <---
First, we'll start by trying to figure out the unknown probability of success associated with a Binom(3,p) random 
variable. If you want to try this on your own later, the following code will perform draws from a binomial with 5 
trials. You can simply change the associated value of p to whatever you'd like. To make the inference blind, have 
a friend set this value and perform the draws from the Binomial for you, without revealing the value of p that they 
used.
"""

from scipy.stats import binom

n = 5
p = 0.5 # Change this and repeat

data = binom.rvs(n,p)

"""
For the in-class version of this exercise, I'm going to perform a manual draw from a binomial using colored marbles 
in a cup. We'll arbitrarily define dark marbles as successes and light marbles as failures.
Record the outcomes here:
Draw 1: dark
Draw 2: dark
Draw 3: dark
Draw 4: dark
Draw 5: dark
Number of 'successes': 5
Now record the observed number of succeses as in the data variable below.
"""

k = 3  # Supply observed number of successes here.
n = 5

"""
Since we are trying to learn about p, we define the likelihood function as;
L(p;data) = P(data|p)
If data is a binomially distributed random variable [data ~ Binom(5,p)]
P(data=k|p) = (5 choose k) * p^k * (1-p)^(n-k)
So, we need a function to calculate the binomial PMF. Luckily, you should have just written one and posted it to 
GitHub for your last exercise. Copy and paste your binomial PMF code below. For now, I will refer to this function 
as binomPMF(). 
"""
def psuFact(minimum,maximum):
    m = maximum
    for i in range(1,maximum):
        z = m - i 
        if z >= minimum:
            maximum = maximum * z
        else: quit
    return maximum

def binCo(n,k):
    return psuFact((n-k+1),n) / psuFact(1,k)
    
def binPMF(p,n,k):
    return int(binCo(n,k))*pow(p,k)*pow((1-p),(n-k))

"""
Now we need to calculate likelihoods for a series of different values for p to compare likelihoods. There are an 
infinite number of possible values for p, so let's confine ourselves to steps of 0.05 between 0 and 1.
"""

# Set up a list with all relevant values of p


p_list = []
x = 0
y = .05
for i in range (25):
    if x < 1:
        x = x + y
        x = round(x,2)
        p_list.append(x)
    else: 
        break

# Calculate the likelihood scores for these values of p, in light of the data you've collected

def likeScores(p_values):
    like_scores = []
    for p in p_values:
        ls = binPMF(p,n,k)
        like_scores.append(ls)
    return like_scores
likeScores(p_list)

# Find the maximum likelihood value of p (at least, the max in this set)

PVal = likeScores(p_list) 
MaxPVal_index = PVal.index(max(PVal))
MaxPVal = PVal[MaxPVal_index]
print MaxPVal
# What is the strength of evidence against the most extreme values of p (0 and 1)?
# If the p values were either 0 or 1, then the observed k value would have to be either 0 or 5 respectively.

# Calculate the likelihood ratios comparing each value (in the numerator) to the max value (in the denominator)
like_Ratio = [round((s/MaxPVal),3) for s in PVal]
print(like_Ratio)


"""
Now let's try this all again, but with more data. This time, we'll use 20 draws from our cup of marbles.
"""

k = 13  # Supply observed number of successes here.
n = 20


# Calculate the likelihood scores for these values of p, in light of the data you've collected

def likeScores(p_values):
    like_scores = []
    for p in p_values:
        ls = binPMF(p,n,k)
        like_scores.append(ls)
    return like_scores
likeScores(p_list)

# Find the maximum likelihood value of p (at least, the max in this set)

PVal = likeScores(p_list) 
MaxPVal_index = PVal.index(max(PVal))
MaxPVal = PVal[MaxPVal_index]
print MaxPVal

# What is the strength of evidence against the most extreme values of p (0 and 1)?
# If the p values were either 0 or 1, then the observed k value would have to be either 0 or 5 respectively.


# Calculate the likelihood ratios comparing each value (in the numerator) to the max value (in the denominator)

like_Ratio = [round((s/MaxPVal),3) for s in PVal]
print(like_Ratio)

# When is the ratio small enough to reject some values of p?
"""
like_Ratio = [round((s/MaxPVal),3) for s in PVal]
print(like_Ratio)
[0.0, 0.0, 0.0, 0.0, 0.001, 0.006, 0.024, 0.079, 0.199, 0.401, 0.662, 
 0.9, 1.0, 0.891, 0.61, 0.296, 0.087, 0.011, 0.0, 0.0]
first four and the last two
"""

"""
Sometimes it will not be feasible or efficient to calculate the likelihoods for every
value of a parameter in which we're interested. Also, that approach can lead to large
gaps between relevant values of the parameter. Instead, we'd like to have a 'hill
climbing' function that starts with some arbitrary value of the parameter and finds
values with progressively better likelihood scores. This is an ML optimization
function. There has been a lot of work on the best way to do this. We're going to try
a fairly simple approach that should still work pretty well, as long as our likelihood 
surface is unimodal (has just one peak). Our algorithm will be:
(1) Calculate the likelihood for our starting parameter value (we'll call this pCurr)
(2) Calculate likelihoods for the two parameter values above (pUp) and below (pDown)
our current value by some amount (diff). So, pUp=pCurr+diff and pDown=pCurr-diff. To
start, set diff=0.1, although it would be nice to allow this initial value to be set
as an argument of our optimization function.
(3) If either pUp or pDown has a better likelihood than pCurr, change pCurr to this
value. Then repeat (1)-(3) until pCurr has a higher likelihood than both pUp and
pDown.
(4) Once L(pCurr) > L(pUp) and L(pCurr) > L(pDown), reduce diff by 1/2. Then repeat
(1)-(3).
(5) Repeat (1)-(4) until diff is less than some threshold (say, 0.001).
(6) Return the final optimized parameter value.
Write a function that takes some starting p value and observed data (k,n) for a
binomial as its arguments and returns the ML value for p.
To write this function, you will probably want to use while loops. The structure of
these loops is
while (someCondition):
    code line 1 inside loop
    code line 2 inside loop
    
As long as the condition remains True, the loop will continue executing. If the
condition isn't met (someCondition=False) when the loop is first encountered, the 
code inside will never execute.
If you understand recursion, you can use it to save some lines in this code, but it's
not necessary to create a working function.
"""

def HillClimber(p,n,k): 
    adjust = 0.1
    thresh = 0.001
    Like_start = binPMF(p,n,k)
    Like_plus = binPMF((p+adjust),n,k)
    Like_minus = binPMF((p-adjust),n,k)
    while (adjust > thresh):
        while (Like_start < Like_plus) or (Like_start < Like_minus):
            if Like_minus > Like_start:
                Like_start -= adjust
            elif Like_plus > Like_start:
                Like_start += adjust
            Like_start = binPMF(p,n,k)
            Like_plus = binPMF((p+change),n,k)
            Like_minus = binPMF((p-change),n,k)
        adjust *= 0.5
        Like_start = binPMF(p,n,k)
        Like_minus = binPMF(p-adjust,n,k)
        Like_plus = binPMF(p+adjust,n,k)
    return p


"""
In the exercise above, you tried to find an intuitive cutoff for likelihood ratio
scores that would give you a reasonable interval in which to find the true value of 
p. Now, we will empirically determine one way to construct such an interval. To do 
so, we will ask how far away from the true value of a parameter the ML estimate 
might stray. Use this procedure: (1) start with a known value for p, (2) simulate
a bunch of datasets, (3) find ML parameter estimates for each simulation, and then 
(4) calculate the likelihood ratios comparing the true parameter values and the ML
estimates. When you do this, you will be constructing a null distribution of
likelihood ratios that might be expected if the value of p you picked in (1)
was true. Note that the ML values for these replicates are very often greater than
L(true value of P), because the ML value can only ever be >= L(true value). Once 
you have this distribution, find the likelihood ratio cutoff you need to ensure 
that the probability of seeing an LR score that big or greater is <= 5%. 
"""

# Set a starting, true value for p

trueP = 0.83

# Simulate 1,000 datasets of 200 trials from a binomial with this p
# If you haven't already done so, you'll want to import the binom class from scipy:
# from scipy.stats import binom
# binom.rvs(n,p) will then produce a draw from the corresponding binomial.

from scipy.stats import binom
import math
import sys

reps = 1000
trials = 200

sims = [] #Create an empty list to store simultion output
for i in range(reps):
    if i % 100 == 0: # If the remainder when divided by 100 is not 0
        print (i),
        sys.stdout.flush() # forces stdout to "flush" the buffer, meaning that it will force everything to print, even if normally it would wait before doing so.
    sims.append(binom.rvs(trials,trueP)) #Use scipy to generate likelihood values given the trueP

# Now find ML parameter estimates for each of these trials

ML_PE = []
for i in range(reps):
    if i % 100 == 0: # If the remainder when divided by 100 is not 0
            print (i),
            sys.stdout.flush() # forces stdout to "flush" the buffer, meaning that it will force everything to print, even if normally it would wait before doing so.
    ML_PE.append(HillClimber(.5,trials,sims[i])) #Use HillClimber function to find the ML estimates

# Calculate likelihood ratios comparing L(trueP) in the numerator to the maximum
# likelihood (ML) in the denominator. Sort the results and find the value
# corresponding to the 95th percentile.

LikeRats = [] 
for i in range(reps):
    if i % 100 == 0: # If the remainder when divided by 100 is not 0
            print (i),
            sys.stdout.flush() # forces stdout to "flush" the buffer, meaning that it will force everything to print, even if normally it would wait before doing so.
    LikeRats.append(-2*math.log(binPMF(trueP,trials,sims[i])/binPMF(ML_PE[i],trials,sims[i])))# Determine Maximum Likelihood i/max[i]
LikeRats.sort() #Sortthe likelihoods
LikeRats_95perc = LikeRats[int(math.floor(reps*0.95))] #Return the largest integer value less than or equal to reps*0.95
print(LikeRats_95perc) 

# Now, convert the likelihood ratios (LRs) to -2ln(LRs) values.
# Find the 95th percentile of these values. Compare these values to this table:
# https://people.richland.edu/james/lecture/m170/tbl-chi.html. In particular, look
# at the 0.05 column. Do any of these values seem similar to the one you calculated?
# Any idea why that particular cell would be meaningful?

# Based on your results (and the values in the table), what LR statistic value 
# [-2ln(LR)] indicates that a null value of p is far enough away from the ML value
# that an LR of that size is <=5% probable if that value of p was true?



# Using this cutoff, what interval might you report for the 5- and 20-trial data
# sets above?



# We've talked in previous classes about two ways to interpret probabilities. Which
# interpretation are we using here to define these intervals?
