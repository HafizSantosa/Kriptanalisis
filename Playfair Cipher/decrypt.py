import numpy as np

# Fungsi untuk membuat matriks Playfair
def build_playfair_matrix(key):
    key = key.upper().replace("J", "I")
    key_chars = []
    for char in key:
        if char not in key_chars and char.isalpha():
            key_chars.append(char)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for char in alphabet:
        if char not in key_chars:
            key_chars.append(char)
    matrix = np.array(key_chars).reshape(5, 5)
    return matrix

# Fungsi dekripsi pasangan
def decrypt_pair(pair, matrix):
    pos = {}
    for i in range(5):
        for j in range(5):
            pos[matrix[i][j]] = (i, j)
    a, b = pair[0], pair[1]
    row_a, col_a = pos[a]
    row_b, col_b = pos[b]

    if row_a == row_b:
        plain_a = matrix[row_a][(col_a - 1) % 5]
        plain_b = matrix[row_b][(col_b - 1) % 5]
    elif col_a == col_b:
        plain_a = matrix[(row_a - 1) % 5][col_a]
        plain_b = matrix[(row_b - 1) % 5][col_b]
    else:
        plain_a = matrix[row_a][col_b]
        plain_b = matrix[row_b][col_a]
    return plain_a + plain_b

new_key = "CRYPTOGRAPHY"  
new_matrix = build_playfair_matrix(new_key)

# Simpan matriks key 
with open("key_matrix.txt", "w") as file:
    file.write("Matriks Kunci:\n")
    for row in new_matrix:
        file.write(" ".join(row) + "\n")

print("Matriks kunci disimpan di 'key_matrix.txt'.")

# Baca ciphertext dari file
with open("cipher.txt", "r") as file:
    ciphertext = file.read().strip()

# Baca matriks terakhir (dari key_matrix.txt)
with open("key_matrix.txt", "r") as file:
    lines = file.readlines()[1:]
    matrix = np.array([list(line.strip().replace(" ", "")) for line in lines])

# Fungsi dekripsi
def decrypt(ciphertext, matrix):
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        pair = ciphertext[i:i+2]
        plaintext += decrypt_pair(pair, matrix) 
    return plaintext

# Jalankan dekripsi
full_decrypted = decrypt(ciphertext, matrix)

# Simpan hasil dekripsi
with open("plaintext.txt", "w") as file:
    file.write("Pesan Terdekripsi:\n")
    file.write(full_decrypted)

print("Dekripsi selesai. Hasil disimpan di 'plaintext.txt'.")