import random

def are_relatively_prime(a,b):
    while b > 0:
        a, b = b, a % b

    return (a == 1)

def modular_inverse_calculator(n, e):
    old_r, r = n, e
    old_s, s = 1, 0
    old_d, d = 0, 1

    while r > 0:
        quotient = old_r // r
        old_r, r = r, old_r-quotient*r
        old_s, s = s, old_s-quotient*s
        old_d, d = d, old_d-quotient*d
    
    if old_d < 0:
        old_d += n

    return old_d


def rsa_setup(p,q):
    #PART I, STEP I
    n = p*q
    phi = (p-1)*(q-1)    #totient

    #PART I, STEP II
    e = random.randint(2, phi-1)
    while are_relatively_prime(e, phi)==False:
        e = random.randint(2, phi-1)

    #PART I, STEP III
    d = modular_inverse_calculator(phi, e)

    return n, e, d

def encrypt(n, e, message):
    publicKey = n,e

    #PART II, STEP 1
    #Converting message to int if presented as a string
    
    #PART II, STEP II    
    encMessage = (message**e)%n

    return encMessage

def decrypt(n, d, encMessage):

    privateKey = d
    
    #PART III, STEP I
    decMessage = (encMessage**d)%n

    #PART III, STEP II
    #Convert message back to a string from int if applicable.

    return message
