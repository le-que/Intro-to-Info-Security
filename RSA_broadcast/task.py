from decimal import *
import math
def isqrt(n, k):
    u, s = n, n+1
    while u < s:
        s = u
        t = (k - 1) * s + n // pow(s, k-1)
        u = t // k
    return s

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
        
def get_multiplicative_inverse(m, a):
    g, x, y = egcd(a, m)
    return x % m
        
def rsa_broadcast_attack(N_1: int, c_1: int, N_2: int, c_2: int, N_3: int, c_3: int) -> int:
    # TODO: Write the necessary code to retrieve the decrypted message (m) using three different
    # ciphers (c_1, c_2, and c_3) created using three different public key N's (N_1, N_2, and N_3)
    m = 42
    # your code starts here: to calculate the original message - m
    # Note 'm' should be an integer
    N_1_i = get_multiplicative_inverse(N_1, N_2*N_3)
    N_2_i = get_multiplicative_inverse(N_2, N_1*N_3)
    N_3_i = get_multiplicative_inverse(N_3, N_2*N_1)
    alpha = N_1_i*N_2*N_3
    beta = N_2_i*N_1*N_3
    gamma = N_3_i*N_1*N_2
    
    m = isqrt((c_1*alpha + c_2*beta + c_3*gamma) % (N_1*N_2*N_3), 3)
    return m
