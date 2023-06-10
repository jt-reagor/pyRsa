# copy of modular exponentiation function in keysetup.py
def modexp(x, a, n):
    abin = bin(a)[2:]
    z = 1
    for bit in abin:
        if bit == '1':
            z = ((z*z%n) * x) % n
        else:
            z = z*z%n
    return z


# encrypt m via modular exponentiation using public key
def encrypt(m, n, e):
    c = modexp(m, e, n)
    return c


def main():
    pubkeyf = open("./public_key", "r")
    messagef = open("./message", "r")

    # get key from file and message
    key_str = pubkeyf.read().splitlines()
    n = int(key_str[0])
    e = int(key_str[1])
    m = int(messagef.read())

    pubkeyf.close()
    messagef.close()

    c = encrypt(m, n, e)  # encrypt message
    with open("./ciphertext", "w") as f:  # write ciphertext to file
        f.write(str(c))


if __name__ == "__main__":
    main()
