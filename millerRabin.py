from random import randint
from esCompuesto import esCompuesto, descomponerBase2
from compTime import compTime

def MillerRabin(n, s):
    (t, u) = descomponerBase2(n)
    for i in range(s):
        a = randint(2, n - 1)
        if esCompuesto(a, n, t, u):
            return False
    return True

@compTime
def getPrimeNumbers(a, b, s):
    list=[]
    for i in range(a, b):
        if MillerRabin(i, s):
            list.append(i)
    return list

if __name__ == "__main__":
    #print(len(getPrimeNumbers(100, 100000, 50))) 
    #--> Resulta 9567
    print(len(getPrimeNumbers(100, 100000, 4)))
    #--> Resulta 9567
    #print(len(getPrimeNumbers(100, 100000, 3))) 
    #--> Resulta 9567+K, el resultado cambia
