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
    for i in range(a, b):
        if MillerRabin(i, s):
            print(i)

if __name__ == "__main__":
    getPrimeNumbers(100, 100000, 50)