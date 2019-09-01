# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 19:44:26 2019

@author: Joshua Rhodes
"""

def gcd(x,y):
    '''
    type x, y == int; 
    output: greatest common factor
    '''
    common_factors = []
    
    for i in range(1,max(x,y)):
        if x % i == 0 and y % i == 0:
            common_factors.append(i)
            
    return max(common_factors)

def phi(x):
    '''
    type x = int;
    returns the number of relatively prime integers less than x
    '''
    value = 0 
    
    for i in range(1,x):
        if gcd(x,i) == 1:
            value += 1
            
    return value

#print(phi(100))

def isPrime(n):
    '''
    type n == int;
    returns boolean: True if n prime, False if n not prime
    '''
    count = 0
    
    for i in range(1,n):
        if gcd(n,i) == 1:
            count += 1
           
    if count == n-1 and n != 1:
        return True
    else:
        return False

def pi(x):
    '''
    type x == int;
    returns number of primes leq x
    '''
    value = 0
    
    for i in range(x+1):
        if isPrime(i) == True:
            value += 1
    
    return value

#print(pi(100))
    
    
    
    
