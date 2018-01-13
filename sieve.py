import math
import sys

def main(n):
    primes = find_primes(n)
    print("Primes are ", primes[:])
    
def find_primes(n):
    if type(n) == float:
        print("Warning: float given. Mapping input to integer")
    n = int(n)
    primes = range(2, n)
    for i in range(2, n):
        if i in primes:
            for p, num in enumerate(primes):
                if num % i ==0 and num != i:
                    primes.pop(p)
    
    return primes
    
if __name__=="__main__":
    if len(sys.argv) > 1:
        n = sys.argv[1]
        main(n)
    else:
        n = input("I will find all the primes less than ...: ")
        main(n)
