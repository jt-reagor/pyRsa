import random


# performs modular exponentiaion via method taught in class
# x^a (mod n)
def modexp(x, a, n):
    abin = bin(a)[2:]  # converts exponent to binary string
    z = 1  # accumulator
    for bit in abin:
        if bit == '1':
            z = ((z*z % n) * x) % n
        else:
            z = z*z % n
    return z


# fermat's primality test
def f_test(p, trials):  # p is the number to test, trials is how many times to perform the test
    for i in range(trials):
        a = random.randint(2, p-1)  # sets a to random number for base pf a^p-1 (mod p)
        if modexp(a, p-1, p) != 1:
            return False
    return True


# generate a large prime with binary length n
def get_prime(n):
    while True:
        p_str = "0b1"  # initialize binary string with leading 1
        for i in range(n-2):
            p_str += str(random.randint(0, 1))  # randomly add 1s and 0s to string
        p_str += "1"  # finish with a 1 to make sure it is odd. Quickly eliminates all even values
        p = int(p_str, 2)  # convert to decimal
        if f_test(p, 2):  # perform 2 rounds of fermat's primality test
            return p  # return p if probable prime, else make a new number


# extended euclidean algorithm
def eea(val1, val2):
    q = 1  # quotient column value
    r1 = val1  # remainder 1
    r2 = val2  # remainder 2 (next remainder)
    c1r1 = 1  # column 1 row 1
    c1r2 = 0  # column 1 row 2
    c2r1 = 0  # column 2 row 1
    c2r2 = 1  # column 2 row 2
    while r2 != 0:  # while remainder not 0
        q = r1 // r2  # get floor of quotient of remainders
        temp = r1  # shift remainders down
        r1 = r2
        r2 = temp % r2  # compute next remainder

        # compute next column 1 val and shift down
        temp = c1r2
        c1r2 = c1r1 - (c1r2 * q)
        c1r1 = temp

        # compute next column 2 val and shift down
        temp = c2r2
        c2r2 = c2r1 - (c2r2 * q)
        c2r1 = temp
    return c1r1, c2r1


# compute two primes with binary length 750 (about 226 decimal) and check to see if valid
def find_2_primes():
    while True:
        p1 = get_prime(750)
        p2 = get_prime(750)
        if len(str(p1 - p2)) > 95:
            return p1, p2


# create key
def gen_key():
    p, q = find_2_primes()  # get our two primes for n
    n = p*q
    e = 65537  # using a set e
    dmod = (p-1)*(q-1)  # d's modulus
    if dmod % e == 0:  # check if d's modulus and e are relatively prime. If they are not, generate new primes
        print("Not relatively prime")
        n, e, d = gen_key()
        return n, e, d
    d, trash = eea(e, dmod)  # calculate d via eea (e's inverse mod dmod)
    d = d % dmod  # make sure to clean up result (mod dmod)
    return n, e, d


def main():
    n, e, d = gen_key()  # get key
    with open("./public_key", "w") as f:  # write public key (n,e) to file
        f.write(str(n)+"\n"+str(e))
    with open("./private_key", "w") as f:  # write private key (d) to file
        f.write(str(d))
    return n, e, d


if __name__ == "__main__":
    main()
