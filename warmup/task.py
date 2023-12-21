
def rsa_decrypt_cipher(n: int, d: int, c: int) -> int:
    m = 0
    # TODO: Write the necessary code to get the message (m) from the cipher (c)
    d = bin(d).replace("0b", "")
    #m = c ** d % n
    e = 1
    for num in d:
        e = e**2*c**int(num) % n
    return e

def rsa_encrypt_message(m: int, e: int, n: int) -> int:
    c = 0
    # TODO: Write the necessary code to get the cipher (c) from the message (m)
    c = m ** e % n
    return c

def rsa_calculate_private_key(e: int, p: int, q: int) -> int:
    d = 0
    phin = (p-1) * (q-1)
    d = pow(e, -1, phin)
    # TODO: Write the necessary code to get the private key d from
    # the public exponent e and the factors p and q
    return d