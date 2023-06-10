# copy of modular exponentiation function in keysetup.py
def modexp(x, a, n):
    abin = bin(a)[2:]
    z = 1
    for bit in abin:
        if bit == '1':
            z = ((z*z % n) * x) % n
        else:
            z = z*z % n
    return z


# decrypt ciphertext using n from public key and d from private key
def decrypt(c, n, d):
    m = modexp(c, d, n)
    return m


def main():
    pubkeyf = open("./public_key", "r")
    privkeyf = open("./private_key", "r")
    cipherf = open("./ciphertext", "r")

    # get key and ciphertext from files
    key_str = pubkeyf.read().splitlines()
    n = int(key_str[0])
    c = int(cipherf.read())
    d = int(privkeyf.read())

    pubkeyf.close()
    privkeyf.close()
    cipherf.close()

    m = decrypt(c, n, d)  # decrypt message
    with open("./decrypted_message", "w") as f:  # write message to file
        f.write(str(m))


if __name__ == "__main__":
    main()
