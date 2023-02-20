# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 15:08:08 2020

@author: super
"""

# import files here
from math import sin 
from math import cos
from math import sqrt
from math import atan
from math import pi
# 4A Write your functions below
# E.g., a function which takes an integer and squares it
# def squared 
def squared(x):
    xx = x**2
    return xx

## DO NOT CHANGE THE FUNCTION NAMES!! ##
# (1)  def twocubedplusone
def twocubedplusone(x):
    return 2*x**3+1



#(2) def sumanddiff
def sumanddiff(x,y):
    return x+y,abs(x-y)




#(3) def sin2cos2
def sin2cos2(x):
    return sin(x)**2+cos(x)**2



#(4) def lucas
def lucas(n):
    i=2
    l_prev,l=2,1
    lucas_list=[2,1]
    while i<n:
        l_prev,l=l,l+l_prev
        i=i+1   
        lucas_list.append(l)
    return lucas_list
   
   
        
    




#(5) def polartocartesian
def polartocartesian(r,theta):
    if -pi<theta<pi and r>0:
     return r*cos(theta),r*sin(theta)
    else:
        return 'theta out of range or r must be positive'
    



#(6) def cartesiantopolar
def cartesiantopolar(x,y):
    if x<0 and y>0:
        return sqrt(x**2+y**2),pi+atan(y/x)
    if x<0 and y<0:
        return sqrt(x**2+y**2),-pi+atan(y/x)
    if x==0 and y>0:
        return sqrt(x**2+y**2),pi/2
    if x==0 and y<0:
        return sqrt(x**2+y**2),-pi/2



## DO NOT CHANGE THE FUNCTION NAMES!!
# 4B
# 
#(1) def horner(x,coeffs):
def horner(x,coeffs):
    coeffs.reverse()
    b=0
    for a in coeffs:
        b = a+x*b
    return b


#(2)
print(horner(4, [1,5,0,1]))
print(horner(sqrt(3),[4,0,-1]))
# Are the answers exact?
# The second answer is not exact. It should be exactly 1

#(3)
# def hornerderiv
def hornerderiv(x,coeffs):
    coeffs.reverse()
    c_coeffs=[]
    c=0
    for a in coeffs:
        c=a+x*c
        c_coeffs.append(c)
    c_coeffs.reverse()
    c_coeffs.remove(c_coeffs[0])
    coeffs.reverse()
    return horner(x,coeffs),horner(x, c_coeffs)
#(4)
# e.g., 
print(hornerderiv(1,[0,0,1,5,0,0,0,-1]))
print(hornerderiv(pi,[0,0,1,5,0,0,0,-1]))

#(5)
print(horner(pi/3,[0,1,0,-1/6,0,1/120,0,-1/5040]))