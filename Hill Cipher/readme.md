# Hill Cipher Cryptanalysis

## 1. Masalah

Kita punya:

    Pesan rahasia (ciphertext): huruf acak "CDECCZDKQ..."

    Sedikit petunjuk (plaintext): "HELLOCYBERFOXATTACKERHERE"

Tugas: temukan cara mengubah ciphertext kembali ke plaintext asli.

## 2. Cara Kerja Hill Cipher

    Enkripsi menggunakan matriks angka sebagai kunci

    Setiap huruf diubah ke angka (A=0, B=1,..., Z=25)

    Pesan dibagi menjadi blok-blok (misal 3 huruf)

    Setiap blok dikalikan dengan matriks kunci

## 3. Langkah Pemecahan
#### a. Diketahui

    Potong plaintext & ciphertext yang diketahui:
    Copy

    Plain: HELLOCYBERFOX...
    Cipher: CDECCZDKQFYR...

#### b. Buat Matriks

    Ambil 9 huruf pertama (untuk matriks 3x3):
    Copy

    Plain: H E L L O C Y B E
    Angka: 7 4 11 11 14 2 24 1 4

    Cipher: C D E C C Z D K Q
    Angka: 2 3 4 2 2 25 3 10 16

#### c. Hitung Matriks Kunci

    Susun angka plaintext jadi matriks 3x3 (P)

    Susun angka ciphertext jadi matriks 3x3 (C)

    Cari invers matriks P (P⁻¹)

    Kalikan C × P⁻¹ untuk dapat kunci (K)

#### d. Dekripsi

    Cari invers matriks kunci (K⁻¹)

    Untuk setiap 3 huruf ciphertext:

        Ubah ke angka

        Kalikan dengan K⁻¹

        Ubah kembali ke huruf

### 4. Contoh

Misal kita punya:

    Plain: "ABC" (0,1,2)

    Cipher: "DEF" (3,4,5)
    
    Hitung matriks kunci: K = Cipher × (Plain)^-1

    Lalu untuk dekripsi: Plain = K⁻¹ × Cipher

### 5. Hasil

```
HELLO CYBER FOX ATTACKER HERE

CRYPTOGRAPHY IS CRUCIAL FOR SAFEGUARDING INFORMATION IN COMPUTING SYSTEMS AND PLAYS AN ESSENTIAL ROLE IN MODERN SECURITY. IT ENABLES SECURE COMMUNICATION, PROTECTS DATA FROM UNAUTHORIZED ACCESS, AND ENSURES DATA INTEGRITY.

THIS TEXT DEMONSTRATES THE POWER OF HILL CIPHER AS A CLASSICAL ENCRYPTION METHOD. ALTHOUGH MODERN CRYPTOSYSTEMS ARE MORE COMPLEX, UNDERSTANDING THESE FUNDAMENTAL ALGORITHMS IS VITAL FOR ANY CYBERSECURITY PROFESSIONAL.

THE HILL CIPHER EXEMPLIFIES HOW MATHEMATICS CAN BE APPLIED TO CREATE SECURE COMMUNICATION CHANNELS. IN REAL WORLD APPLICATIONS, CRYPTOGRAPHY IS USED IN VARIOUS DOMAINS INCLUDING ONLINE TRANSACTIONS, DIGITAL SIGNATURES, PASSWORD STORAGE, AND MANY MORE.

THIS EXERCISE HAS SUCCESSFULLY DEMONSTRATED HOW KNOWN PLAINTEXT ATTACKS CAN BREAK CLASSICAL CIPHERS, WHICH UNDERSCORES THE IMPORTANCE OF USING MODERN SECURE ENCRYPTION METHODS FOR REAL WORLD SECURITY NEEDS.
```
    