import math
import eea
import random
import prime

def RSA_keygen(n=100):
    
    p = prime.generate_primes(n=n, k=1)[0]
    q = prime.generate_primes(n=n, k=1)[0]
   
    n = p * q
  
    phi_n = (p - 1) * (q - 1)
  
    while True:
        e = random.randrange(1, phi_n-1)
        if math.gcd(e, phi_n) == 1:
        
            gcd, s, t = eea.EEA(phi_n, e)
            if gcd == (s*phi_n + t*e):
                d = t % phi_n
                break
    return (e, n, d, len(str(n).strip()))

if __name__ == '__main__':
    print(RSA_keygen())