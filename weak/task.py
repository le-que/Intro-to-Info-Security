import math
import typing

def rsa_weak_key_attack(given_public_key_N: int, given_public_key_e: int, public_key_list: typing.List[int]) -> int:
    # TODO: Write the necessary code to retrieve the private key d from the given public
    # key (N, e) using only the list of public keys generated using the same flawed RNG
    d = 0
    for public_key in public_key_list:
        q = math.gcd(given_public_key_N, public_key)
        if q != 1:
            break
    p = given_public_key_N // q
    d = pow(given_public_key_e, -1, (p - 1) * (q - 1))
    return d
