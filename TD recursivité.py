from timeit import default_timer as timer
from random import randint

#1°
def factorielle(n):
    S=1
    for nb in range(1,n+1):
        S*=nb
    return S

print(factorielle(5))

#2°
def ISomme(n):
    S=0
    for nb in range(n+1):
        S+=nb
    return S

def RSomme(n):
    if n==1:
        return 1
    else:
        return n+RSomme(n-1)

print(ISomme(5))
print(RSomme(5))

#3°
def minimum(a,b):
    if a<b:
        return a
    else:
        return b

def miniIt(L):
    mini=L[0]
    for i in range(1,len(L)-1):
        mini=minimum(mini,L[i])
    return mini

def miniRec(L):
    if len(L)==1:
        return L[0]
    else:
        return minimum(L[0],miniRec(L[1:]))

L=[randint(0,100) for i in range(999)]
debut=timer()
print(miniIt(L))
fin=timer()
print(fin-debut)

debut=timer()
print(miniRec(L))
fin=timer()
print(fin-debut)
