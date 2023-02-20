# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 15:02:55 2020

@author: super
"""

#MATH2920 Miniproject Pythagorean Triples and EUler Bricks Template File

#import files here
from math import gcd
from math import log
from math import pi
from math import sqrt
import matplotlib.pyplot as plt


#Part 1
#1a
def PrimPyth(n):
    triples = []
    p = 2
    q = 1
    while p**2+q**2<n:
        if 1<gcd(p,q)<p or p%2>0 and q%2>0:
            q+=1
        else:
            triples.append((p**2-q**2,2*p*q,p**2+q**2))
            q+=1
        if gcd(p,q) ==p:
            p+=1
            q = 1
    return triples
        
#1b function call and graph
triples = []
p = 2
q = 1
while p**2+q**2<10000:
        if 1<gcd(p,q)<p or p%2>0 and q%2>0:
            q+=1
        else:
            triples.append((p**2-q**2,2*p*q,p**2+q**2))
            q+=1
        if gcd(p,q) ==p:
            p+=1
            q=1
            
plt.figure('Figure A')
x = [triples[i][0] for i in range(len(triples))]
y = [triples[i][1] for i in range(len(triples))]
plt.plot(x,y,'o')


#1c
def Pyth(n):
    triples = []
    p = 2
    q = 1
    t = 1
    while t*(p**2+q**2)<n:
        if 1<gcd(p,q)<p or p%2>0 and q%2>0:
            q+=1
        else:
            triples.append((t*(p**2-q**2),2*p*q*t,t*(p**2+q**2)))
            t+=1
        if t*(p**2+q**2)>=n:
            q+=1
            t=1
        if q==p:
            p+=1
            q=1
            t=1
    return triples
    
#1d function call and graph
triples_2 = []
p = 2
q = 1
t = 1
while t*(p**2+q**2)<10000:
        if 1<gcd(p,q)<p or p%2>0 and q%2>0:
            q+=1
        else:
            triples_2.append((t*(p**2-q**2),2*p*q*t,t*(p**2+q**2)))
            t+=1
        if t*(p**2+q**2)>=10000:
            q+=1
            t=1
        if q==p:
            p+=1
            q=1
            t=1
        
            
plt.figure('Figure B')
a = [triples_2[i][0] for i in range(len(triples_2))]
b = [triples_2[i][1] for i in range(len(triples_2))]
plt.plot(a,b,'o')

#1e Comment
#Figure B looks like the points are creating an arc of a circle of radius 10000.
#Which makes sense since all the triangles with hypotenuse less than 10000 lie in that circle
#There seems to be ray lines pertruding from the centre which shows that all triples are multiples
#of primitive triples so the gradient of the ray lines is constant 

#Figure A looks like the points are bounded by some sort of curve there are
#also more gaps indicating that the distribution of primitive triples is less predictable
#than regular triples. There are also curved lines curving upwards from the centre. It
#makes sense that the lines are curved since if they were straight,not all the triples would
#be primitive. 

#Part 2
#2a
def CuboidFaces(s,t):
    c=0
    d=0
    if s==t:
        return False
    for i in range(len(t)):
        if s[0]==t[i]:
            c+=1
        if s[1]==t[i]:
            d+=1
    if c==2 and d==0 or d==2 and c==0 or c==1 or d==1:
        return True
    else:
        return False
        
#2b
def Bricks(n):
    triples = []
    Cuboid_sides = []
    sides = []
    p = 2
    q = 1
    t = 1
    i = 0
    j = 0
    while t*(p**2-q**2)<n and t*(2*p*q)<n:
        if 1<gcd(p,q)<p or p%2>0 and q%2>0:
            q+=1
        else:
            triples.append((t*(p**2-q**2),2*p*q*t,t*(p**2+q**2)))
            t+=1
        if t*(p**2-q**2)>=n or t*(2*p*q)>=n :
            q+=1
            t=1
        if q==p:
            p+=1
            q=1
            t=1
    while i<len(triples):
       if CuboidFaces((triples[i][0],triples[i][1]),(triples[j][0],triples[j][1]))==True:
           triples_list = (triples[i][0],triples[i][1],triples[j][0],triples[j][1]) 
           triples_list = list(dict.fromkeys(triples_list))
           if len(triples_list) == 3:
                Cuboid_sides.append((triples_list[0],triples_list[1],triples_list[2]))
       j+=1
       if j==len(triples)-1:
           i+=1
           j=0
    for i in range(len(Cuboid_sides)):
        if sqrt((Cuboid_sides[i][0])**2+(Cuboid_sides[i][1])**2)%1==0 and sqrt((Cuboid_sides[i][0])**2+(Cuboid_sides[i][2])**2)%1==0 and sqrt((Cuboid_sides[i][1])**2+(Cuboid_sides[i][2])**2)%1==0:
            if (Cuboid_sides[i][0],Cuboid_sides[i][1],Cuboid_sides[i][2]) not in sides and (Cuboid_sides[i][0],Cuboid_sides[i][2],Cuboid_sides[i][1]) not in sides and (Cuboid_sides[i][2],Cuboid_sides[i][0],Cuboid_sides[i][1]) not in sides and (Cuboid_sides[i][2],Cuboid_sides[i][1],Cuboid_sides[i][0]) not in sides and (Cuboid_sides[i][1],Cuboid_sides[i][2],Cuboid_sides[i][0]) not in sides and (Cuboid_sides[i][1],Cuboid_sides[i][0],Cuboid_sides[i][2]) not in sides:
               sides.append(Cuboid_sides[i])
    return sides
           
#2c function call and comment
triples = []
Cuboid_sides = []
sides = []
p = 2
q = 1
t = 1
i = 0
j = 0
while t*(p**2-q**2)<1000 and t*(2*p*q)<1000:
        if 1<gcd(p,q)<p or p%2>0 and q%2>0:
            q+=1
        else:
            triples.append((t*(p**2-q**2),2*p*q*t,t*(p**2+q**2)))
            t+=1
        if t*(p**2-q**2)>=1000 or t*(2*p*q)>=1000 :
            q+=1
            t=1
        if q==p:
            p+=1
            q=1
            t=1
while i<len(triples):
       if CuboidFaces((triples[i][0],triples[i][1]),(triples[j][0],triples[j][1]))==True:
           triples_list = (triples[i][0],triples[i][1],triples[j][0],triples[j][1]) 
           triples_list = list(dict.fromkeys(triples_list))
           if len(triples_list) == 3:
                Cuboid_sides.append((triples_list[0],triples_list[1],triples_list[2]))
       j+=1
       if j==len(triples)-1:
           i+=1
           j=0
for i in range(len(Cuboid_sides)):
        if sqrt((Cuboid_sides[i][0])**2+(Cuboid_sides[i][1])**2)%1==0 and sqrt((Cuboid_sides[i][0])**2+(Cuboid_sides[i][2])**2)%1==0 and sqrt((Cuboid_sides[i][1])**2+(Cuboid_sides[i][2])**2)%1==0:
            if (Cuboid_sides[i][0],Cuboid_sides[i][1],Cuboid_sides[i][2]) not in sides and (Cuboid_sides[i][0],Cuboid_sides[i][2],Cuboid_sides[i][1]) not in sides and (Cuboid_sides[i][2],Cuboid_sides[i][0],Cuboid_sides[i][1]) not in sides and (Cuboid_sides[i][2],Cuboid_sides[i][1],Cuboid_sides[i][0]) not in sides and (Cuboid_sides[i][1],Cuboid_sides[i][2],Cuboid_sides[i][0]) not in sides and (Cuboid_sides[i][1],Cuboid_sides[i][0],Cuboid_sides[i][2]) not in sides:
               sides.append(Cuboid_sides[i])
print(len(sides))
#There are 10 Euler Bricks with dimension less than 1000 5 of which 
#(140,480,693),(44,117,240),(132,85,720),(140,480,693),(252,240,275) and (160,231,792) are primitive
#which means that the greatest common multiple of the sides is 1


#Part 3
# Pythagorean quadruples and interesting limit:
def Pyth_2(n):
    quadruples = []
    a = 1
    b = 1
    p = gcd(a,b)
    t = 1
    while a+b+((a**2+b**2-(p*t)**2)/(2*p*t))+((a**2+b**2+(p*t)**2)/(2*p*t))<n and (p*t)**2<a**2+b**2:
        if a%2==0 and b%2==0 and p%2>0:
            t+=1
        if a%2==1 and b%2==1:
            b+=1
        else:
           quadruples.append((a,b,((a**2+b**2-(p*t)**2)/(2*p*t)),((a**2+b**2+(p*t)**2)/(2*p*t))))
           t+=1
        if (p*t)**2>=a**2+b**2:
            b+=1
            t=1
        if a+b+(a**2+b**2-(p*t)**2)/(2*p*t)+(a**2+b**2+(p*t)**2)/(2*p*t)>=n:
            a+=1
            b=1
            t=1   
    return(quadruples)
#attempted to create quadruples but couldn't create a list of integer quadruples
        
        
def Perimeter(n):
    triples = []
    p = 2
    q = 1
    t = 1
    while t*(p**2+q**2)+t*(p**2-q**2)+2*p*q*t<n:
        if 1<gcd(p,q)<p or p%2>0 and q%2>0:
            q+=1
        else:
            triples.append((t*(p**2-q**2),2*p*q*t,t*(p**2+q**2)))
            t+=1
        if t*(p**2+q**2)>=n:
            q+=1
            t=1
        if q==p:
            p+=1
            q=1
            t=1
    return len(triples)


    

#plt.figure('Figure C')
#a = [(Perimeter(n))/n for n in range(1,100001)]
#b = [n for n in range(1,100001)]
#plt.plot(b,a,'o')
#c = [(log(2)/((pi)**2)) for n in range(1,100001)]
#plt.plot(b,c)
#graph shows that the limit is true as most of the points lie on the line of the limit line given by c

