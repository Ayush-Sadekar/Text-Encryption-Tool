from ciphers import caesar_cipher, vigenere_cipher

print("Text Encryption Tool")
print("1 - Caesar Cipher")
print("2 - Vigenere Cipher")

cipher = input("Choose 1/2: ")
phrase = input("Enter your phrase: ")


if cipher == "1":
    shift = int(input("Enter the shift number: "))
    mode = input("Choose encryption or decryption (e/d): ").lower()

    if mode == "e":
        result = caesar_cipher(phrase, shift, mode = 'encrypt')
    else:
        result = caesar_cipher(phrase, shift, mode = 'decrypt')

elif cipher == "2":
    shift = input("Enter the keyword: ")
    mode = input("Choose encryption or decryption (e/d): ").lower()

    if mode == "e":
        result = vigenere_cipher(phrase, shift, mode = 'encrypt')
    else:
        result = vigenere_cipher(phrase, shift, mode = 'decrypt')
else:
    print("Invalid Choice")

print("Result:")
print(result)


