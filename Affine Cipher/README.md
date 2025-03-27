# Affine Cipher

Affine Cipher adalah salah satu teknik kriptografi klasik yang merupakan kombinasi dari **Caesar Cipher** dan **Multiplicative Cipher**. Cipher ini bekerja dengan menggunakan fungsi matematis berbasis **modular aritmetika** untuk melakukan enkripsi dan dekripsi teks.

### **Rumus Enkripsi**

Setiap huruf dalam **plaintext** $P$ dikonversi ke angka berdasarkan urutan alfabetnya (**A = 0, B = 1, ..., Z = 25**), lalu dienkripsi dengan rumus:

$$C = (aP + b)\mod 26$$

Di mana:

- $C$ = Karakter terenkripsi (**ciphertext**)
- $P$ = Karakter asli (**plaintext**)
- $a$ = **Kunci multiplikatif** (harus memiliki invers modulo 26, artinya **gcd(a, 26) = 1**)
- $b$ = **Kunci aditif** (shift)

### **Rumus Dekripsi**

Untuk mendekripsi teks yang sudah dienkripsi, digunakan rumus:

$$P = a^{-1} (C - b) \mod 26$$

Di mana $a^{-1}$ adalah **modular inverse** dari $a$ modulo 26, yang memenuhi:

$$a \cdot a^{-1} \equiv 1 \mod 26$$

Dengan menggunakan **modular inverse**, kita dapat mengembalikan **ciphertext** menjadi **plaintext** dengan mudah.

## Dokumentasi Langkah-Langkah Analisis

Dalam soal, dijelaskan bahwa Cyber Fox memiliki kode Python yang berfungsi untuk mengenkripsi gambar dalam bentuk byte. Fungsi `affine_cipher(hex_values, m, b, n)` menerapkan Affine Cipher pada setiap byte gambar dengan rumus:

$$𝐶=(𝑚⋅𝑃+𝑏)\mod  𝑛$$

Di mana:

- `m` dan `b` adalah bilangan acak yang dipilih.
- `n` = 256 (karena setiap byte dalam gambar memiliki nilai 0-255).

Di dalam kode tersebut, nilai `m` dan `b` diacak menggunakan `random.randint` antara angka 1 hingga 256, jadi kita tidak mengetahui nilai dari kedua variable tersebut. Nilai `m` dipastikan akan memiliki invers modulo `n` karena adanya kondisi `math.gcd(m, n) == 1` pada fungsi main.

Karena tidak mengetahui nilai `m` dan `b`, kita dapat mencarinya menggunakan **invers modulo** agar bisa membuat kode dekripsinya. Untuk menghitung invers modulo, kita dapat menggunakan rumus yang saya tulis di atas. Namun agar lebih mudah, kita dapat menggunakan kode Python untuk menghitungnya.

Untuk membantu perhitungan, Cyber Fox memiliki clue untuk nilai P dan C, yaitu **P₁ = 0xFF = 255, C₁ = 0xB7 = 183** dan **P₂ = 0xD8 = 216, C₂ = 0x32 = 50**. Dengan clue tersebut, berarti kita memiliki 2 persamaan, yaitu:

$$(m×255+b)\mod256=183$$
$$(m×216+b)\mod256=50$$

Dengan ini, kita dapat dengan lebih mudah untuk mencari `m` dan `b`.

## Kode Python untuk Menghitung Nilai m dan b

Berikut adalah kode yang digunakan untuk mencari `m` dan `b`.

```py
import math

P1, C1 = 0xFF, 0xB7
P2, C2 = 0xD8, 0x32
n = 256

def find_affine_keys(P1, C1, P2, C2, n):
    delta_P = (P1 - P2) % n
    delta_C = (C1 - C2) % n

    try:
        m = (delta_C * pow(delta_P, -1, n)) % n
    except ValueError:
        return "Tidak ada solusi, karena delta_P tidak memiliki invers modulo."

    b = (C1 - m * P1) % n

    return m, b

m, b = find_affine_keys(P1, C1, P2, C2, n)
print(f"Nilai m: {m}")
print(f"Nilai b: {b}")
```

**Penjelasan:**

- Untuk mencari nilai `m`, kita menggunakan persamaan berikut:
  $$m = \frac{P_1 - P_2}{C_1 - C_2} \mod n$$
  Karena pembagian dalam modulus harus menggunakan modular inverse, kita gunakan `pow(delta_P, -1, n)` untuk mendapatkan invers modular dari **delta_P**.
- Untuk mencari nilai `b`, kita hanya perlu subtitusikan ke persamaan berikut:
  $$b=(C1−m×P1)\mod n$$

## Kunci Nilai m dan b

Berdasarkan perhitungan di atas, nilai `m` adalah **115** dan nilai `b` adalah **42**.

## Kode Python untuk Dekripsi

Berikut adalah kode Python untuk mendekripsi gambar:

```py
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
```

**Penjelasan:**

- Menggunakan algoritma Affine Cipher untuk mendekripsi setiap byte berdasarkan rumus:
  $$ 𝑃=𝑚−1×(𝐶−𝑏)\mod𝑛 $$
  Di mana:

  - 𝑃 adalah pixel asli setelah dekripsi.
  - 𝐶 adalah pixel terenkripsi.
  - $𝑚^{-1}$ adalah invers modular dari 𝑚.
  - 𝑏 adalah konstanta pergeseran.
  - 𝑛 adalah 256 (karena byte gambar berada dalam rentang 0-255).

- Mengonversi kembali hasil dekripsi ke dalam bentuk bytearray.
- Menyimpan hasil bytearray ke dalam file gambar baru.

## Gambar hasil dekripsi

Berikut adalah gambar hasil dekripsi:
[img](decrypted.jpeg)

## Perbandingan dengan pendekatan Brute Force / Exhaustive Key Attack (optional)

Kita mencoba untuk menggunakan metode Brute Force, yang di mana kita hanya perlu menebak nilai `m` dan `b` dari range 1 hingga 256 dan mencoba beberapa kemungkinannya. Kode yang menggunakan metode Brute Force sudah saya cantumkan pada `bruteforce.py`.

## Waktu kriptanalisis yang dibutuhkan

Metode analisis matematika dan brute force memiiki waktu yang mirip, di sekitar **0,00125** detik.
