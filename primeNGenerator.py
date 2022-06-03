from millerRabin import MillerRabin
from random import randint
from compTime import compTime

def randomBits(b):
    pow2 = pow(2, b - 1)
    n = randint(0, pow2  * 2 - 1)
    m = pow2 + 1
    n = n | m
    return n

def genPrimoBits(b, s):
    n = randomBits(b)
    while not MillerRabin(n, s):
        n = n + 2
    return n

def genPrimoMayor(n, s):
    n = n + 1 - (n % 2)
    while not MillerRabin(n, s):
        n = n + 2
    return n

@compTime
def getPrimes(s):
    list_16=[]
    list_32=[]
    list_64=[]
    print("Primos de 16 bits: ")
    while len(list_16)!=10:
        a=genPrimoBits(16,s)
        if (a not in list_16):
            list_16.append(a)
        else:
            i=i-1
    print(list_16)
    print("Primos de 32 bits: ")
    while len(list_32)!=10:
        a=genPrimoBits(32,s)
        if (a not in list_32):
            list_32.append(a)
        else:
            i=i-1
    print(list_32)

    print("Primos de 64 bits: ")
    while len(list_64)!=10:
        a=genPrimoBits(64,s)
        if (a not in list_64):
            list_64.append(a)
        else:
            i=i-1
    print(list_64)

if __name__ == "__main__":
    getPrimes(326)
