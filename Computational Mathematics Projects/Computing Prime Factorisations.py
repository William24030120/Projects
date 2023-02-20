# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 16:05:54 2020

@author: super
"""

# import files here
from math import gcd
from math import floor
from math import sqrt
# Function to generate primes by Eratosthenes' sieve
def eratosthenes(max_prime):
    primes = list(range(2,max_prime+1))
    for i in primes:
        j=2
        while i*j<= primes[-1]:
            if i*j in primes:
                primes.remove(i*j)
            j=j+1
    return primes

# 5A Write your functions below
# E.g., a function which takes an integer and squares it
# def semiprime_factorisation1

def semiprime_factorisation1(n):
    possible_factors = eratosthenes(n)
    for i in possible_factors:
        for j in possible_factors:
            if i*j == n:
                return i, j
    return None

## DO NOT CHANGE THE FUNCTION NAMES!! ##

def euler_phi(n):
    t=1
    for i in range(1,n):
        if gcd(i,n) == 1:
            t+=1
        if gcd(i,n) > 1:
            t=t
    return t 
    
     
    
    
    
    




def semiprime_factorisation2(n):
    factors = []
    for  i in range(2,floor(sqrt(n))+1):
        if n%i == 0:
            factors.append(i)
            factors.append(n//i)
    return factors
            
    



def prime_factorisation(n):
    prime_factors = []
    j=2
    while n>1:
        if n%j == 0:
            prime_factors.append(j)
            n=n//j
        else:
            j=j+1
    return prime_factors


