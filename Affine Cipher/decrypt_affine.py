import os

def affine_decipher(cipher_hex, m_inv, b, n):
    plain_hex = []
    for hex_value in cipher_hex:
        P = hex((m_inv * (int(hex_value, 16) - b)) % n)
        plain_hex.append(P)
    return plain_hex

def read_image_to_hex(image_path):
    try:
        with open(image_path, "rb") as image:
            f = image.read()
            b = bytearray(f)
            array_of_hex = [hex(byte) for byte in b]
        return array_of_hex
    except FileNotFoundError:
        print("Error: File not found.")
        return None

def array_of_hex_to_bytearray(array_of_hex):
    bytearray_data = bytearray()
    for hex_value in array_of_hex:
        if hex_value.startswith('0x'):
            hex_value = hex_value[2:]
        byte_value = int(hex_value, 16)
        bytearray_data.append(byte_value)
    return bytearray_data

def create_file_from_bytes(file_path, bytes_data):
    try:
        with open(file_path, "wb") as file:
            file.write(bytes_data)
        print("File berhasil dibuat:", file_path)
    except Exception as e:
        print("Error:", e)

def main_decrypt(encrypted_image_path, output_image_path):
    n = 256
    m_inv = 187  
    b = 42

    if not os.path.exists(encrypted_image_path):
        print(f"Error: File '{encrypted_image_path}' tidak ditemukan.")
        return
    
    hex_values = read_image_to_hex(encrypted_image_path)
    if hex_values is not None:
        plain_hex = affine_decipher(hex_values, m_inv, b, n)
        bytearray_plain = array_of_hex_to_bytearray(plain_hex)
        create_file_from_bytes(output_image_path, bytearray_plain)
        print("Dekripsi selesai!")

main_decrypt("affinecipher.jpeg", "decrypted.jpeg")
