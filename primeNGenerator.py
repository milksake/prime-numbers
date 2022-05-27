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
    for i in range(10):
        print(genPrimoBits(16, s))
    for i in range(10):
        print(genPrimoBits(32, s))
    for i in range(10):
        print(genPrimoBits(64, s))

if __name__ == "__main__":
    getPrimes(2)