def rot15(ct):
    result = []
    for char in ct:
        if char.isalpha():
            shift = 11
            base = ord('a') if char.islower() else ord('A')
            shifted_char = chr(base + (ord(char) - base + shift) % 26)
            result.append(shifted_char)
        else:
            result.append(char)
    
    return ''.join(result)
cipherText = "WAANDTUAAZAJYTTVDAVIARDCCXQL"
decoded = rot15(cipherText)
print("Decoded:", decoded)
