def caesar(message, offset):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted = []
    for char in message:
        if char.lower() not in alphabet:
            encrypted.append(char)
        else:
            pos = alphabet.index(char.lower())
            shifted = (pos + offset) % len(alphabet)
            new_char = [alphabet[shifted], alphabet[shifted].upper()][char.isupper()]
            encrypted.append(new_char)



    return "".join(encrypted)


print(caesar("G jmtc Nwrfml Yaybckw", 2))