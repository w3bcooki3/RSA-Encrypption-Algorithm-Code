import math
import random

#-------------------------------------------------------#
# Rabin Miller's Primality test

def Miller_Rabin_test(num):
    a = num - 1
    b = 0
    while a % 2 == 0:
        a = a // 2
        b += 1
    for _ in range(40): # _ means any variable
        rand = random.randrange(2, num - 1)
        c = pow(rand, a, num)
        if c != 1:
            i = 0
            while c != (num - 1):
                if i == b - 1:
                    return False
                else:
                    i = i + 1
                    c = (c ** 2) % num
    return True

#---------------------------------------------------------#
# Function to generate random Prime number
def random_prime(k_size):
    while True:
        prime = random.randrange(2 ** (k_size - 1), 2 ** (k_size))
        if prime_check(prime) and prime % 2==1:
            return prime

# This function is to check whether the number selected is prime or not
def prime_check(number):

    if (number <= 1):
        return False

    prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
    if number in prime:
        return True
    for i in prime:
        if (number % i == 0):
            return False
    return Miller_Rabin_test(number)


# Assigning bits to s
def MRT(s = 512):
    return random_prime(s)

# Euclidean Algorithm code
def EA(r1, r2):
    while(r1!=0):
        r2, r1 = r1, (r2 % r1)
    return r2

# Extended Euclidean Algorithm code
def EEA(r1, r2):
    if(r1 % r2 == 0):
        return(r2, 0, 1)
    else:
        gcd, s, t = EEA(r2, r1 % r2)
        s = s - ((r1 // r2) * t)
        return(gcd, t, s)

# Square and multiply Algorithm code
def powmod_sm(x, y, p):
	res = 1
	x = x % p
	if (x == 0):
		return 0
	while (y > 0):
		if ((y & 1) == 1):
			res = (res * x) % p
		y = y >> 1
		x = (x * x) % p
	return res

# Function to calculate the value of d by finding the modular inverse e
def inverse(e, r):
    gcd, s, _ = EEA(e, r)
    if(gcd != 1):
        return None
    else:
        return s % r

# RSA key generation using the above functions
def keyGeneration():
    p = MRT() #p = random prime number
    q = MRT() #q = random prime number

    n = p * q
    phi = (p - 1) * ( q - 1)
    #print('\nCalculating value of n\n:~~~> ',n)
    #print("\nCalculating value of phi\n:~~~>",phi)

    #Choosing value of e randomly
    for i in range(1, 1000):
        if(EA(i, phi) == 1):
            e = i

   # print("\nCalculating the value of e:~~~>", e)

    #print('***********************************************************************')

    # Help taken from google to find d
    d = inverse(e, phi)

    # dic will store the RSA keys with value
    dic = {}
    dic['public_key'] = (e, n)
    dic['private_key'] = (d, n)
    return dic

# We will use this function to encrypt our input
def encryption(public_key, plaintext):
    e, n = public_key
    x = []
    cipher = ""
    m = 0
    for i in plaintext:
        m = ord(i) #Change charater to Unicode
        t = powmod_sm(m,e,n)
        x.append(t)
        cipher+=str(t)
        cipher+=','
    return cipher[:-1]

# We will use this function to decrypt our input
def decryption(private_key, ciphertext):
    d, n = private_key
    plaintext = list(map(int, ciphertext. split(',')))
    x = ''
    m = 0
    for i in plaintext:
        m = powmod_sm(i, d, n)
        t = chr(m)
        x += t
    return x


def main():

    print('***********************************************************************')

    ques = input("Welcome!\n\tEnter your secret MESSAGE ~~~~~>  ")

    print('***********************************************************************')

    #Let's generate RSA Public and Private Key pairs
    RSA_keys = keyGeneration()
    public_key = RSA_keys['public_key']
    private_key = RSA_keys['private_key']

    #Now we encrypt our input by calling the decryption function below
    ciphertext = encryption(public_key, ques)
    print("\nOscar is upset because you used encryption. :~~~~~> \n")
    print("\U0001F606 \U0001F606 \U0001F606 \U0001F606 \U0001F606 \U0001F606 \U0001F606 \U0001F606 \U0001F606 \U0001F606 \U0001F606 \U0001F606 \U0001F606 \U0001F606 \U0001F606 \U0001F606 \U0001F606 \U0001F606 \U0001F606 \U0001F606 \U0001F606 \U0001F606 \U0001F606 \U0001F606 \U0001F606 \U0001F606 ")
    print(ciphertext)

    print("\U0001F606 \U0001F606 \U0001F606 \U0001F606 \U0001F606 \U0001F606 \U0001F606 \U0001F606 \U0001F606 \U0001F606 \U0001F606 \U0001F606 \U0001F606 \U0001F606 \U0001F606 \U0001F606 \U0001F606 \U0001F606 \U0001F606 \U0001F606 \U0001F606 \U0001F606 \U0001F606 \U0001F606 \U0001F606 \U0001F606 ")

    #Decryption of our Input
    plaintext = decryption(private_key, ciphertext)
    print('\nPlease do not decrypt me, I want Oscar to try hard :)\nAnyways, here is your decrypted text. :~~~~~~~~~~~~~>', plaintext)

    print('\U0001F62A \U0001F62A \U0001F62A \U0001F62A \U0001F62A \U0001F62A \U0001F62A \U0001F62A \U0001F62A \U0001F62A \U0001F62A \U0001F62A \U0001F62A \U0001F62A \U0001F62A \U0001F62A \U0001F62A \U0001F62A \U0001F62A \U0001F62A \U0001F62A \U0001F62A \U0001F62A \U0001F62A \U0001F62A \U0001F62A ')

    print('\n')


main()
