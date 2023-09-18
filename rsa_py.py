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


#TEST METHOD
"""
primes = [11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631]

trials = 30
count = 0
for i in range(trials):
    p, q = random.sample(primes, 2)
    n,e,d = rsa_setup(p, q)
    print(p,q,n,e,d)
    message = (random.randint(1, n-1))
    en = encrypt(n, e, message)
    print(en)
    if message != decrypt(n, d, en):
        print("Error for p={0} q={1}".format(p,q))
        count += 1

print(f"Error rate {count/trials}")
"""
