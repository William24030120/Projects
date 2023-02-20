# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 15:02:23 2020

@author: super
"""

#Template for Week 8 Exercises

# import files here
from random import shuffle
from time import perf_counter
import matplotlib.pyplot as plt
import numpy as np
from math import log

# Question 1 code
def selectionsort(mylist):
    sortedlist = []
    while len(mylist) > 0:
        lowest = mylist[0]
        for x in mylist:
            if x < lowest:
                lowest = x
        sortedlist.append(lowest)
        mylist.remove(lowest)
    return sortedlist

issvalues = []
sssorttimelist = []
time_end = perf_counter()
for i in range(1, 11):
  issvalues.append(2**i)
  mylist = list(range(2**i))
  shuffle(mylist)
  time_start = perf_counter()
  selectionsort(mylist)
  time_end = perf_counter()
  sorttime = time_end-time_start
  sssorttimelist.append(sorttime)

   
# Question 2 code
plt.figure('Figure A')
plt.title('Log-Log plot of time taken to sort lists')
plt.xlabel('Log of the size of the lists')
plt.ylabel('Log of the time taken to sort list')
a = issvalues
b = sssorttimelist
plt.loglog(a,b, label = 'Selection Sort Algorithm')
plt.legend(loc = 'upper left')

# Question 2 comment
#the gradient:(log(sssorttimelist[9])-log(sssorttimelist[0]))//(log(1024)-log(2)) equals 1.4 approxiamtely, hence t_s(i) is approximately O(x)


#Question 3 code for bubblesort:
def bubblesort(mylist):
    i=len(mylist)-1
    while i>0:
        for j in range(0,i):
            if mylist[j]>mylist[j+1]:
                mylist[j],mylist[j+1] = mylist[j+1],mylist[j]
        i=i-1

    return mylist            

ibsvalues = []
bssorttimelist = []
for i in range(1, 11):
  ibsvalues.append(2**i)
  mylist = list(range(2**i))
  shuffle(mylist)
  time_start = perf_counter()
  bubblesort(mylist)
  time_end = perf_counter()
  sorttime = time_end-time_start
  bssorttimelist.append(sorttime)


# Question 4 code 
plt.figure('Figure B')
plt.title('Log-Log plot of time taken to sort lists')
plt.xlabel('Log of the size of the lists')
plt.ylabel('Log of the time taken to sort list')
a = issvalues
b = sssorttimelist
plt.loglog(a,b, label = 'Selection Sort Algorithm')
c = ibsvalues
d = bssorttimelist
plt.loglog(c,d, label = 'Bubble Sort Algorithm')
plt.legend(loc = 'upper left')

#Question 5 code 
def mergesort ( mylist ):
    if len ( mylist ) <= 1:
        return mylist
    
    m = len ( mylist ) // 2        
    l = mergesort ( mylist [: m ])
    r = mergesort ( mylist [ m :])    
    result = []
    i = j = 0
    while (len (result) < len (r)+ len (l)):
         if l [ i ] < r [j ]:
              result . append ( l [ i ])
              i = i +1
         else:
              result . append ( r [ j ])
              j = j +1
         if i == len(l) or j == len(r):
             result.extend(l[i:] or r[j:])
             break
    return result

imsvalues = []
mssorttimelist = []
for i in range(1,11):
  imsvalues.append(2**i)
  mylist = list(range(2**i))
  shuffle(mylist)
  time_start = perf_counter()
  mergesort(mylist)
  time_end = perf_counter()
  sorttime = time_end-time_start
  mssorttimelist.append(sorttime)


plt.figure('Figure C')
plt.title('Log-Log plot of time taken to sort lists')
plt.xlabel('Log of the size of the lists')
plt.ylabel('Log of the time taken to sort list')
a = issvalues
b = sssorttimelist
plt.loglog(a,b, label = 'Selection Sort Algorithm')
c = ibsvalues
d = bssorttimelist
plt.loglog(c,d, label = 'Bubble Sort Algorithm')
e = imsvalues
f = mssorttimelist
plt.loglog(e,f, label = 'Merge Sort Algorithm')
plt.legend(loc = 'upper left')
#Question 5 comment
# The graph shows that the gradient (1.15) of the mergesort is shallower than selectionsort with gradient 1.4, and selectionsort is faster than O(x^2). So mergesort must be faster than O(x^2)
    
    
#Question 6 code
itsvalues = []
tssorttimelist = []
for i in range(1,11):
  itsvalues.append(2**i)
  mylist = list(range(2**i))
  shuffle(mylist)
  time_start = perf_counter()
  sorted(mylist)
  time_end = perf_counter()
  sorttime = time_end-time_start
  tssorttimelist.append(sorttime)


plt.figure('Figure D')
plt.title('Log-Log plot of time taken to sort lists')
plt.xlabel('Log of the size of the lists')
plt.ylabel('Log of the time taken to sort list')
g = itsvalues
h = tssorttimelist
plt.loglog(g,h, label = 'Timsort Algorithm')
e = imsvalues
f = mssorttimelist 
plt.loglog(e,f, label = 'Mergesort Algorithm')
plt.legend(loc = 'upper left')

#Question 6 comment
#As the graph shows, mergesort takes longer than timsort as the mergesort (orange) line is above the timsort (blue) line. 


#Question 7 code
def countingsort(mylist):
    returnlist = []
    N = max(mylist)
    bucketlist = [0 for i in range(N+1)]
    j=0
    k=0
    while k<len(mylist):
        if mylist[k] == j:
            bucketlist[j] = bucketlist[j]+1
        j+=1
        if j == N+1:
            k+=1
            j=0
    for i in range(N+1):
       returnlist.append(i*bucketlist[i])
    return returnlist
           
#Question 8 code
icsvalues = []
cssorttimelist = []
for i in range(1,11):
  icsvalues.append(2**i)
  mylist = list(range(2**i))
  shuffle(mylist)
  time_start = perf_counter()
  countingsort(mylist)
  time_end = perf_counter()
  sorttime = time_end-time_start
  cssorttimelist.append(sorttime)


plt.figure('Figure E')
plt.title('Log-Log plot of time taken to sort lists')
plt.xlabel('Log of the size of the lists')
plt.ylabel('Log of the time taken to sort list')
a = issvalues
b = sssorttimelist
plt.loglog(a,b, label = 'Selection Sort Algorithm')
c = ibsvalues
d = bssorttimelist
plt.loglog(c,d, label = 'Bubble Sort Algorithm')
e = imsvalues
f = mssorttimelist
plt.loglog(e,f, label = 'Merge Sort Algorithm')
g = icsvalues
h = cssorttimelist
plt.plot(g,h, label = 'Counting Sort Algorithm')
plt.legend(loc = 'upper left')

#Question 8 comment
# Counting sort is inefficient when the integers to be sorted are much larger than the number of integers to be sorted. So a list like [10837,20938028,2098231] would be very inefficient. But a list like: {1,2,3,4,5,6,7,8,9,10} would be very efficient.
# The graph shows that countingsort has a steeper gradient than the mergesort and selectionsort algorithms suggesting that is has a higher complexity and is therefore less efficient. Counting sort seems to have a similar gradient to bubble sort suggesting that they maybe of similar complexity.
# The countingsort line is above the other three lines meaning that the countingsort algorithm is not as fast as the other three algortithms.