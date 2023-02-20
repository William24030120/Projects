# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 12:59:32 2020

@author: super
"""

#Exercise 6A solutions 

#import modules here
import matplotlib.pyplot as plt
import numpy as np



#Exercise 6A(i)
def collatzseq(n):
    collatzseq_=[n]
    while n>1:
        if n%2==0:
            n=n/2
            collatzseq_.append(n)
        elif n%2==1:
            n=3*n+1
            collatzseq_.append(n)
    return collatzseq_
        
    
         
    

    

#Exercise 6A(ii)
def collatzcount(n):
   i=0
   while n>1:
        if n%2==0:
            n=n/2
            i+=1
        elif n%2==1:
            n=3*n+1
            i+=1
   return i



#Exercise 6A(iii)

#Write your code that plots your graph here (not commented out)
x = np.arange(0,1001,1)
y = [collatzcount(z) for z in x]
plt.plot(x,y,'o')
plt.xlabel('x')
plt.ylabel('Collatzcount(x)')
plt.title('Number of steps needed for x to get to 1')
plt.figure('Figure A')
    
#Exercise 6A(iv)
#44.3%
#k=0
#for n in x:
#    if collatzcount(n)<n/10:
#        k+=1
#print((k/1000)*100)
        

#Exercise 6A(v)
a = np.arange(0,10001,1)
b = [max(collatzseq(z)) for z in a]
plt.plot(a,b)
plt.xlabel('x')
plt.ylabel('Highest number reached in Collatzseq(x)')
plt.title('Highest number reached in the collatz sequence starting with x')
plt.figure('Figure B')

plt.figure('Figure C')
plt.loglog(a,b)
plt.xlabel('log(x)')
plt.ylabel('log(Highest number reached in Collatzseq(x))')
plt.title('logarithm plot of the highest number reached in collatzseq(x)')
z = [c for c in a]
plt.plot(a,z)

plt.figure('Figure D')
plt.semilogx(a,b)
plt.xlabel('log(x)')
plt.ylabel('Highest number reached in Collatzseq(x)')
plt.title('Highest number reached in the collatz sequence starting with x')

plt.figure('Figure E')
plt.semilogy(a,b)
plt.xlabel('Highest number reached in Collatzseq(x)')
plt.ylabel('log(Highest number reached in Collatzseq(x))')
plt.title('Highest number reached in the collatz sequence starting with x')
z = [c for c in a]
plt.plot(a,z)

#The function y=x shown in orange seems to approximate the gradient on the loglog graph.
#The function y=x also appears to be a lower bound on the loglog graph and the semilogy graph suggesting that the highest number reached in the sequence can't be less than logx.
#The function semilogx shows that the higher the number x, the higher the maximum number reached by starting the sequence with x.
#The highest number reached in the sequence is always even. It couldn't be odd since an odd number is mapped to a higher number under the collatz sequence.


#Reminder: check your programme runs before submission! Your code should generate any figures when run. Do not upload/submit figures separately.
