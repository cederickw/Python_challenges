import base64
import string

# ROT(n) functie
def rot_n(text, n):
    result = []
    for char in text:
        if char.isalpha():  # Check of het een letter is
            base = ord('a') if char.islower() else ord('A')
            # Verschuif letter en voeg toe aan resultaat
            result.append(chr((ord(char) - base + n) % 26 + base))
        else:
            result.append(char)  # Niet-alfabetische karakters blijven hetzelfde
    return ''.join(result)

# Base64 encoding functie
def base64_encode(text):
    # Converteer string naar bytes
    text_bytes = text.encode('utf-8')
    # Base64 encode
    encoded_bytes = base64.b64encode(text_bytes)
    # Zet bytes terug naar string
    encoded_str = encoded_bytes.decode('utf-8')
    return encoded_str

# Base64 decoding functie
def base64_decode(encoded_str):
    # Zet de base64 encoded string om naar bytes
    encoded_bytes = encoded_str.encode('utf-8')
    # Decodeer Base64 bytes
    decoded_bytes = base64.b64decode(encoded_bytes)
    # Zet bytes terug naar string
    decoded_str = decoded_bytes.decode('utf-8')
    return decoded_str

# Voorbeeld gebruik
if __name__ == "__main__":
    # Keuze voor ROT(n) of Base64
    keuze = input("Wil je ROT(n) of Base64 gebruiken? (rot/base64): ").strip().lower()
    
    if keuze == "rot":
        tekst = input("Voer de tekst in: ")
        verschuiving = int(input("Voer de ROT(n) verschuiving in: "))
        actie = input("Wil je encoderen of decoderen? (encode/decode): ").strip().lower()

        if actie == "encode":
            rot_encoded = rot_n(tekst, verschuiving)
            print(f"ROT({verschuiving}) encoding: {rot_encoded}")
        elif actie == "decode":
            rot_decoded = rot_n(tekst, -verschuiving)
            print(f"ROT({verschuiving}) decoding: {rot_decoded}")
        else:
            print("Ongeldige keuze voor actie.")
    
    elif keuze == "base64":
        tekst = input("Voer de tekst in: ")
        actie = input("Wil je encoderen of decoderen? (encode/decode): ").strip().lower()

        if actie == "encode":
            base64_encoded = base64_encode(tekst)
            print(f"Base64 encoding: {base64_encoded}")
        elif actie == "decode":
            try:
                base64_decoded = base64_decode(tekst)
                print(f"Base64 decoding: {base64_decoded}")
            except Exception as e:
                print(f"Fout tijdens Base64 decoding: {e}")
        else:
            print("Ongeldige keuze voor actie.")
    
    else:
        print("Ongeldige keuze. Kies 'rot' of 'base64'.")
