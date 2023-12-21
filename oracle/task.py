from typing import Callable

# You may find these helpful
import math
from decimal import *


def rsa_parity_oracle_attack(c: int, N: int, e: int, oracle: Callable[[int], bool]) -> str:

    # TODO: Write the necessary code to get the plaintext message from the cipher (c) using
    # the public key (N, e) and an oracle function - oracle(chosen_c) that will give you
    # the parity of the decrypted value of a chosen cipher (chosen_c) value using the hidden private key (d)

    l = 0
    r = 1
    k = 1
    while (N * l // k + 1 < N * r // k):
        m = l + r
        l <<= 1
        r <<= 1
        k <<= 1
        if not oracle(c * pow(k, e, N) % N):
            l = m
        else:
            r = m
    if pow(N * l // k, e, N) == c:
        m_int = int(N * l // k)
    elif pow(N * r // k, e, N) == c:
        m_int = int(N * r // k)
    # # Transform the integer value of the message into a human readable form
    message = bytes.fromhex(hex(int(m_int)).rstrip('L')[2:]).decode('utf-8')

    return message
