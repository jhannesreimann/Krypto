def apply_substitution(ciphertext, substitutions):
    ciphertext_dict = dict(substitutions)
    plaintext = ""

    for char in ciphertext:
        if char in ciphertext_dict:
            plaintext += ciphertext_dict[char]
        else:
            plaintext += char

    return plaintext, ciphertext

def undo_substitution(ciphertext, substitutions):
    reverse_substitutions = [(b, a) for a, b in substitutions]
    return apply_substitution(ciphertext, reverse_substitutions)

def main():
    initial_ciphertext = "PQHKBCD LRNZNTDUHKXHIHQYAZHLKQFKMCU CMHZGTQYAHZKUQZZHKPQHKULMPQHKVRZKFHLARPHZKMZPKLHYAZQBHZKMFKQZORCFNLQRZHZKNMUKVHCUYATMHUUHTLHZKLHELHZKIMKGHJQZZHZKPQHUHKQZORCFNLQRZHZKBRHZZHZKURJRATKPHCKVHCJHZPHLHKUYATMHUUHTKJQHKNMYAKPHCKRCQGQZNTLHELKUHQZKAHMLIMLNGHKXHIHQYAZHLKPHCKXHGCQOOKBCD LRNZNTDUHKNTTGHFHQZHCKPQHKNZNTDUHKVRZKBCD LRGCN AQUYAHZKVHCONACHZKFQLKPHFKIQHTKPQHUHKHZLJHPHCKIMKXCHYAHZKNTURKQACHKUYAMLIOMZBLQRZKNMOIMAHXHZKRPHCKQACHKUQYAHCAHQLKZNYAIMJHQUHZKMZPKIMKSMNZLQOQIQHCHZKBCD LRNZNTDUHKQULKPNFQLKPNUKGHGHZULMHYBKIMCKBCD LRGCN AQH"
    ciphertext = initial_ciphertext
    substitutions = []

    while True:
        print(f"Aktueller Text: ", end="")
        for char in ciphertext:
            if char in dict(substitutions):
                print(f"\033[1;32;40m{char}\033[0m", end="")
            else:
                print(char, end="")
        print(f"\nAktuelle Substitutionen: {substitutions}")
        action = input("Eingabe (a,b) für Substitution oder '-' zum Rückgängig machen: ")

        if action == "-":
            if substitutions:
                substitutions.pop()
                ciphertext, _ = undo_substitution(initial_ciphertext, substitutions)
            else:
                print("Keine Substitutionen vorhanden.")
        elif "," in action:
            a, b = action.split(",")
            substitutions.append((a, b))
            ciphertext, _ = apply_substitution(initial_ciphertext, substitutions)
        else:
            print("Ungültige Eingabe. Bitte (a,b) oder '-' eingeben.")

if __name__ == "__main__":
    main()

# Aktueller Text: PQHKBCD LRNZNTDUHKXHIHQYAZHLKQFKMCU CMHZGTQYAHZKUQZZHKPQHKULMPQHKVRZKFHLARPHZKMZPKLHYAZQBHZKMFKQZORCFNLQRZHZKNMUKVHCUYATMHUUHTLHZKLHELHZKIMKGHJQZZHZKPQHUHKQZORCFNLQRZHZKBRHZZHZKURJRATKPHCKVHCJHZPHLHKUYATMHUUHTKJQHKNMYAKPHCKRCQGQZNTLHELKUHQZKAHMLIMLNGHKXHIHQYAZHLKPHCKXHGCQOOKBCD LRNZNTDUHKNTTGHFHQZHCKPQHKNZNTDUHKVRZKBCD LRGCN AQUYAHZKVHCONACHZKFQLKPHFKIQHTKPQHUHKHZLJHPHCKIMKXCHYAHZKNTURKQACHKUYAMLIOMZBLQRZKNMOIMAHXHZKRPHCKQACHKUQYAHCAHQLKZNYAIMJHQUHZKMZPKIMKSMNZLQOQIQHCHZKBCD LRNZNTDUHKQULKPNFQLKPNUKGHGHZULMHYBKIMCKBCD LRGCN AQH
# Aktueller Text: DIE KRYPTOANALYSE BEZEICHNET IM URSPRUENGLICHEN SINNE DIE STUDIE VON METHODEN UND TECHNIKEN UM INFORMATIONEN AUS VERSCHLUESSELTEN TEXTEN ZU GEWINNEN DIESE INFORMATIONEN KOENNEN SOWOHL DER VERWENDETE SCHLUESSEL WIE AUCH DER ORIGINALTEXT SEIN HEUTZUTAGE BEZEICHNET DER BEGRIFF KRYPTOANALYSE ALLGEMEINER DIE ANALYSE VON KRYPTOGRAPHISCHEN VERFAHREN MIT DEM ZIEL DIESE ENTWEDER ZU BRECHEN ALSO IHRE SCHUTZFUNKTION AUFZUHEBEN ODER IHRE SICHERHEIT NACHZUWEISEN UND ZU QUANTIFIZIEREN KRYPTOANALYSE IST DAMIT DAS GEGENSTUECK ZUR KRYPTOGRAPHIE
# Aktuelle Substitutionen: [('P', 'D'), ('Q', 'I'), ('H', 'E'), ('K', ' '), ('B', 'K'), ('C', 'R'), ('D', 'Y'), (' ', 'P'), ('L', 'T'), ('R', 'O'), ('N', 'A'), ('Z', 'N'), ('T', 'L'), ('U', 'S'), ('X', 'B'), ('I', 'Z'), ('Y', 'C'), ('A', 'H'), ('F', 'M'), ('M', 'U'), ('O', 'F'), ('E', 'X'), ('J', 'W'), ('S', 'Q')]