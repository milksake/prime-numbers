# Prime Numbers

Integrantes:
- Mariana Cáceres Urquizo
- Jorge Núñez Paucar
- Camila Orihuela Flores

## Clonar
      git clone https://github.com/milksake/prime-numbers.git
### Ejecutar primeNgenerator.py
      python3 primeNGenerator.py
### Ejecutar MillerRabin.py
      python3 millerRabin.py
      
## [Miller Rabin](millerRabin.py)
Se llama a la función getPrimeNumbers(a, b, s) siendo "a" el número en el que inicia a buscar, "b" hasta el número que se llegará y "s" el número de veces que se probará si un número es primo en una base aleatoria. 
Dentro se llama a la función MillerRabin(i, s) que imprime un número en caso sea primo.
MillerRabin hace uso de las funciones:
descomponerBase2(n) transforma un número "n" a (2^t)x(u)
esCompuesto(a, n, t, u) Comprueba si un número es compuesto para una base "n"

**Proceso:**
Añadimos todos los números primos generados por el algoritmo a una lista y los contamos con la función len, la longitud de esta lista cambiará si un número compuesto es agregado
Entonces encontramos un valor mínimo para s, 4

## [Generador de primos de 16, 32 y 64 bits](primeNGenerator.py)
Se llama a la función getPrimes()
genPrimoBits(bits, s) siendo "s" las veces que se probara que un número sea primo para varias bases.
Al usar un s=50 tenemos la certeza de que todos los numeros generados por el algoritmo serán primos,entonces podemos reducir "s" hasta empezar a tener resultados inestables.
Al probar "s" en diferentes valores menores a 50 tenemos al 4 como mínimo valor posible para asegurar que se generen numeros primos

**Proceso:**
Se genera un número de 16, 32 o 64 bits y pasamos este número por Miller Rabin con un s=3, caso el número sea primo, será añadido a una lista verificando antes que el número no esté en la lista.
