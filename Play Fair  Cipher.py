def preprocess_text(text):
    text = text.replace("J", "I")  # Gantikan 'J' dengan 'I'
    text = text.upper()  # Ubah teks menjadi huruf besar
    text = "".join(filter(str.isalpha, text))  # Hapus karakter non-alfabet
    return text

def create_playfair_matrix(key):
    key = key.upper()
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # Hilangkan 'J' karena sudah digantikan dengan 'I'
    matrix = []
    for char in key:
        if char not in matrix and char in alphabet:
            matrix.append(char)
    for char in alphabet:
        if char not in matrix:
            matrix.append(char)
    return matrix

def encrypt_playfair(plaintext, key):
    plaintext = preprocess_text(plaintext)
    matrix = create_playfair_matrix(key)
    ciphertext = ""
    i = 0
    while i < len(plaintext):
        if i == len(plaintext) - 1:
            pair = plaintext[i] + "X"
            i += 1
        elif plaintext[i] == plaintext[i + 1]:
            pair = plaintext[i] + "X"
            i += 1
        else:
            pair = plaintext[i] + plaintext[i + 1]
            i += 2
        row1, col1 = divmod(matrix.index(pair[0]), 5)
        row2, col2 = divmod(matrix.index(pair[1]), 5)
        if row1 == row2:
            ciphertext += matrix[row1 * 5 + (col1 + 1) % 5]
            ciphertext += matrix[row2 * 5 + (col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += matrix[((row1 + 1) % 5) * 5 + col1]
            ciphertext += matrix[((row2 + 1) % 5) * 5 + col2]
        else:
            ciphertext += matrix[row1 * 5 + col2]
            ciphertext += matrix[row2 * 5 + col1]
    return ciphertext

def decrypt_playfair(ciphertext, key):
    matrix = create_playfair_matrix(key)
    plaintext = ""
    i = 0
    while i < len(ciphertext):
        pair = ciphertext[i] + ciphertext[i + 1]
        i += 2
        row1, col1 = divmod(matrix.index(pair[0]), 5)
        row2, col2 = divmod(matrix.index(pair[1]), 5)
        if row1 == row2:
            plaintext += matrix[row1 * 5 + (col1 - 1) % 5]
            plaintext += matrix[row2 * 5 + (col2 - 1) % 5]
        elif col1 == col2:
            plaintext += matrix[((row1 - 1) % 5) * 5 + col1]
            plaintext += matrix[((row2 - 1) % 5) * 5 + col2]
        else:
            plaintext += matrix[row1 * 5 + col2]
            plaintext += matrix[row2 * 5 + col1]
    return plaintext

# Contoh penggunaan
key = "selamatmalam"
plaintext = "MIRNAWATI"
encrypted_text = encrypt_playfair(plaintext, key)
print("Plaintext:", plaintext)
print("Encrypted Text:", encrypted_text)
decrypted_text = decrypt_playfair(encrypted_text, key)
print("Decrypted Text:", decrypted_text)