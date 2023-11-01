def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def mod_inverse(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Modulares Inverses existiert nicht')
    else:
        return x % m

def decrypt_affine_cipher(ciphertext, a, b):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    m = len(alphabet)
    a_inverse = mod_inverse(a, m)

    plaintext = ""
    for char in ciphertext:
        if char in alphabet:
            index = alphabet.index(char)
            decrypted_index = (a_inverse * (index - b)) % m
            decrypted_char = alphabet[decrypted_index]
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext

def brute_force_affine_cipher(ciphertext):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    for a in range(1, len(alphabet)):
        if egcd(a, len(alphabet))[0] == 1:
            for b in range(len(alphabet)):
                decrypted_text = decrypt_affine_cipher(ciphertext, a, b)
                if "F" in decrypted_text and "A" in decrypted_text and "M" in decrypted_text and "O" in decrypted_text:
                    print(f"Possible Solution (a={a}, b={b}): {decrypted_text}")

if __name__ == "__main__":
    ciphertext = input("Gib den verschlüsselten Text ein: ")
    brute_force_affine_cipher(ciphertext)

# Aufgabe:
# BAOF OLAYANMAFAXSNEMGFKRSFVOHQMRZOEQYXAF XSBAMFNXCYFXTFBOXMMASFWEYOMELNASBFKROFCYOXNMLN
# (a=26, b=4): DER FRUEHESTE EINSATZ VON KRYPTOGRAPHIE FINDET SICH IM DRITTEN JAHRTAUSEND VOR CHRISTUS