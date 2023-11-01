def decrypt_custom_cipher(ciphertext, shift):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    decryption_dict = {shifted_alphabet[i]: alphabet[i] for i in range(len(alphabet))}
    
    plaintext = ""
    for char in ciphertext:
        if char in decryption_dict:
            plaintext += decryption_dict[char]
        else:
            plaintext += char
    return plaintext

def brute_force_custom_cipher(ciphertext):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    for shift in range(len(alphabet)):
        decrypted_text = decrypt_custom_cipher(ciphertext, shift)
        print(f"Shift {shift}: {decrypted_text}")

if __name__ == "__main__":
    ciphertext = input("Gib den verschlüsselten Text ein: ")
    brute_force_custom_cipher(ciphertext)

# Aufgabe: 
# VBI DZRBL STPKTCDKOTPKGTCCPYCNSLQDKOPBKFPBCNSWEPCCPWEYRKFZYKTYQZBXLDTZY
# KRYPTOGRAPHIE IST DIE WISSENSCHAFT DER VERSCHLUESSELUNG VON INFORMATION
# mit shift 11