## 1. Kriptanalisis Cipher Abjad-Tunggal
Di laboratorium KCKS, Cyber Fox yang penasaran, sedang menyelidiki sebuah anomali dalam sistem jaringan DTI. Saat menelusuri log, Cipher menemukan sebuah dokumen terenkripsi yang mencurigakan. Namun, ada satu masalah: teks dalam dokumen tersebut telah dikodekan menggunakan cipher substitusi abjad-tunggal (monoalphabetic cipher), dan kunci enkripsinya tidak diketahui. Untungnya, Cipher adalah ahli dalam kriptanalisis dan tahu bahwa metode ini bisa dipecahkan menggunakan analisis frekuensi dan terkaan kata. Jika diketahui bahwa bahasa yang digunakan dalam teks adalah bahasa inggris, bantulah Cyber Fox membuat tabel substitusi huruf dan mendekripsi teks sebelum waktunya habis! 

```
LAHYCXPAJYQHRBJWRWMRBYNWBJKUNCXXUOXAYAXCNLCRWPRWOXAVJCRXWRWLXV
YDCRWPBHBCNVBRCRBDBNMNENAHFQNANKHKRUURXWBXOYNXYUNFXAUMFRMNXWJM
JRUHKJBRBBNLDARWPKXCQMJCJJCANBCJWMMJCJRWVXCRXWLAHYCXPAJYQRLBHB
CNVBJANODWMJVNWCJUCXBCJWMJAMYAXCXLXUBVXBCWXCJKUHCQNCAJWBYXACUJ
HNABNLDARCHCUBYAXCXLXUFQRLQNWJKUNBBCAXWPNWLAHYCRXWJLAXBBJFRMNA
JWPNXOJYYURLJCRXWBMNBYRCNRCBRVYXACJWLNLAHYCXPAJYQHRBRWQNANWCUH
OAJPRUNNENWCQNVXBCBNLDANLAHYCXPAJYQRLBHBCNVLJWKNANWMNANMLXVYUN
CNUHRWBNLDANKHJBRWPUNBYNLRORLJCRXWOUJFXAYAXPAJVVRWPNAAXACAJMRC
RXWJUBXOCFJANCNBCRWPVNCQXMBBDLQJBDWRCCNBCRWPJANRWBDOORLRNWCCXD
WLXENABNLDARCHEDUWNAJKRURCRNBRWLAHYCXBHBCNVBRWBCNJMLAHYCXPAJYQ
RLBNLDARCHRBNBCJKURBQNMCQAXDPQVJCQNVJCRLJUVXMNURWPJWMARPXAXDBY
AXXOBMNVXWBCAJCRWPCQJCJBHBCNVVNNCBCQNWNLNBBJAHBNLDARCHYAXYNACR
NBCQNBNJAPDVNWCBXOCNWANUHXWYUJDBRKUNJBBDVYCRXWBCXEJURMJCNCQNRA
LUJRVBXWNXOCQNNJAURNBCJWMBRVYUNBCLAHYCXPAJYQRLCNLQWRZDNBRBCQNL
JNBJALRYQNAFQRLQMJCNBKJLTCXJAXDWMKLCQRBVNCQXMNWLXMNBYUJRWCNGCK
HBQROCRWPNJLQUNCCNAXOCQNJUYQJKNCKHJORGNMWDVKNAXOYXBRCRXWBFQRUN
CQRBJYYAXJLQFJBNOONLCRENJCCQNCRVNMDNCXCQNXKBLDARCHXOCQNVNCQXMR
CYAXERMNBWXANJUBNLDARCHCXMJHBRWLNCQNANJANXWUHYXBBRKUNBQROCBCQN
LRYQNALJWKNNJBRUHKAXTNWCQAXDPQKADCNOXALNMNBYRCNRCBBRVYURLRCHCQ
NLJNBJALRYQNAANVJRWBXWNXOCQNVXBCFRMNUHANLXPWRINMNWLAHYCRXWCNLQ
WRZDNBQXFNENARCXOONABWXANJUYAXCNLCRXWJBRCLJWKNZDRLTUHMNLRYQNAN
MKHQJWMJMMRCRXWJUUHRCBLRYQNACNGCRBNJBRUHRMNWCRORJKUNKNLJDBNCQN
OANZDNWLHMRBCARKDCRXWXOUNCCNABVRAAXABCQJCXOCQNNWPURBQUJWPDJPNC
QRBQRPQURPQCBJTNHYARWLRYUNRWVXMNAWLAHYCXPAJYQHCADNBNLDARCHANUR
NBWXCXWUHXWBNLANLHKDCJUBXXWBCAXWPVJCQNVJCRLJUOXDWMJCRXWBJWMLXV
YDCJCRXWJURWONJBRKRURCH
```

## 1.1 Tabel Frekuensi Kemunculan Huruf dalam Bahasa Inggris

| Huruf | Frekuensi (%) |
|-------|---------------|
| E     | 12.70         |
| T     | 9.06          |
| A     | 8.17          |
| O     | 7.51          |
| I     | 6.97          |
| N     | 6.75          |
| S     | 6.33          |
| H     | 6.09          |
| R     | 5.99          |
| D     | 4.25          |
| L     | 4.03          |
| C     | 2.78          |
| U     | 2.76          |
| M     | 2.41          |
| F     | 2.23          |
| Y     | 2.02          |
| P     | 1.93          |
| B     | 1.49          |
| V     | 0.98          |
| K     | 0.77          |
| X     | 0.15          |
| Q     | 0.10          |
| J     | 0.10          |
| Z     | 0.07          |

data tersebut didapatkan dari https://en.wikipedia.org/wiki/Letter_frequency

## 1.2 Tabel Frekuensi Kemunculan Huruf dalam Cipherteks
| Huruf | Frekuensi (%) |
|-------|---------------|
| N     | 11.38         |
| C     | 9.85          |
| R     | 8.84          |
| B     | 7.63          |
| X     | 7.06          |
| A     | 6.93          |
| J     | 6.87          |
| W     | 6.17          |
| L     | 4.64          |
| Q     | 4.20          |
| U     | 3.88          |
| Y     | 3.56          |
| H     | 3.24          |
| M     | 2.92          |
| D     | 2.48          |
| V     | 2.35          |
| P     | 2.03          |
| O     | 2.03          |
| K     | 1.91          |
| F     | 0.76          |
| E     | 0.51          |
| Z     | 0.25          |
| T     | 0.25          |
| G     | 0.19          |
| I     | 0.06          |

![image](https://github.com/user-attachments/assets/9a3e4b50-4c67-417c-9b57-b13131bbbecc)
# Penjelasan Kode
Berikut adalah penjelasan mendetail mengenai kode Python yang Anda berikan, yang digunakan untuk mendekripsi ciphertext menggunakan metode cipher Caesar.


# Tabel substitusi huruf
| Frekuensi Huruf Cipherteks | Frekuensi Huruf Bahasa Inggris |
|-------------------|-----------------|
| N                 | E               |
| C                 | T               |
| R                 | A               |
| B                 | O               |
| X                 | I               |
| A                 | N               |
| J                 | S               |
| W                 | H               |
| L                 | R               |
| Q                 | D               |
| U                 | L               |
| Y                 | U               |
| H                 | C               |
| M                 | M               |
| D                 | F               |
| V                 | Y               |
| P                 | P               |
| O                 | G               |
| K                 | K               |
| F                 | W               |
| E                 | X               |
| Z                 | Z               |
| T                 | Q               |
| G                 | V               |
| I                 | T               |
# Penjelasan Tabel
lalu kita coba untuk substitusikan hasil dari frekuensi kemunculan huruf dalam bahasa inggris, dan juga frekuensi kemunculan huruf dalam chiperteks.


# Metode Analisis pemecahan cipherteks
Selanjutnya kita bisa mencoba untuk membuat program python otomatis agar memudahkan kita untuk mendekrip cipherteks, kita akan langsung mencoba dengan shift 25
![image](https://github.com/user-attachments/assets/0598d47d-e195-4b4a-a228-65a3fb0769f8)
#### 1. Fungsi `caesar_decrypt`

```python
def caesar_decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                decrypted_text += chr((ord(char) - shift_amount - 97) % 26 + 97)
            elif char.isupper():
                decrypted_text += chr((ord(char) - shift_amount - 65) % 26 + 65)
        else:
            decrypted_text += char
    return decrypted_text
```

- **Parameter**:
  - `ciphertext`: Teks yang akan didekripsi.
  - `shift`: Jumlah pergeseran yang digunakan dalam cipher Caesar.

- **Variabel**:
  - `decrypted_text`: String kosong yang akan diisi dengan hasil dekripsi.

- **Proses**:
  - **Looping**: Untuk setiap karakter (`char`) dalam `ciphertext`:
    - **Cek Huruf**: Jika karakter adalah huruf (menggunakan `isalpha()`):
      - **Hitung Pergeseran**: `shift_amount` dihitung sebagai `shift % 26` untuk memastikan tidak ada pergeseran yang lebih dari 25.
      - **Huruf Kecil**: Jika karakter adalah huruf kecil (`islower()`), maka:
        - `ord(char)` mengembalikan nilai ASCII dari karakter.
        - Rumus `chr((ord(char) - shift_amount - 97) % 26 + 97)` digunakan untuk menghitung huruf yang didekripsi. 
          - `- 97` mengubah huruf menjadi indeks (0 untuk 'a', 1 untuk 'b', dst.).
          - `% 26` memastikan hasilnya tetap dalam rentang 0-25.
          - `+ 97` mengubah kembali indeks menjadi karakter.
      - **Huruf Besar**: Jika karakter adalah huruf besar (`isupper()`), prosesnya mirip, tetapi menggunakan `65` sebagai basis (0 untuk 'A', 1 untuk 'B', dst.).
    - **Karakter Non-Huruf**: Jika karakter bukan huruf, karakter tersebut ditambahkan ke `decrypted_text` tanpa perubahan.
  
- **Return**: Mengembalikan `decrypted_text` yang berisi teks yang telah didekripsi.

#### 2. Fungsi `brute_force_caesar`

```python
def brute_force_caesar(ciphertext):
    for shift in range(1, 26):
        decrypted_text = caesar_decrypt(ciphertext, shift)
        print(f"Shift {shift}: {decrypted_text}")
```

- **Parameter**:
  - `ciphertext`: Teks yang akan didekripsi.

- **Proses**:
  - **Looping**: Untuk setiap nilai `shift` dari 1 hingga 25:
    - Memanggil fungsi `caesar_decrypt` dengan `ciphertext` dan `shift` saat ini.
    - Mencetak hasil dekripsi dengan format `Shift {shift}: {decrypted_text}`.

#### 3. Ciphertext yang Akan Didekripsi

```python
ciphertext = """LAHYCXPAJYQHRBJWRWMRBYNWBJKUNCXXUOXAYAXCNLCRWPRWOXAVJCRXWRWLXV
YDCRWPBHBCNVBRCRBDBNMNENAHFQNANKHKRUURXWBXOYNXYUNFXAUMFRMNXWJM
...
"""
```

- Ini adalah string panjang yang berisi ciphertext yang akan didekripsi.

#### 4. Menjalankan Brute Force

```python
brute_force_caesar(ciphertext)
```

- Memanggil fungsi `brute_force_caesar` untuk mencoba semua kemungkinan pergeseran dari 1 hingga 25 dan mencetak hasilnya.

### Kesimpulan

Kode ini secara efektif mendekripsi teks yang dienkripsi menggunakan cipher Caesar dengan mencoba semua kemungkinan pergeseran. Dengan menggunakan fungsi `caesar_decrypt`, kode ini dapat mengembalikan teks asli dari ciphertext yang diberikan. Hasil dari setiap pergeseran dicetak, sehingga Anda dapat dengan mudah menemukan teks yang masuk akal. 

# Mempersempit Kemungkinan
hasil ditemukan pada pergeseran (shift) 9, menggunakan kode Python yang dapat digunakan untuk mendekripsi ciphertext dengan shift 9:
![A](https://github.com/user-attachments/assets/9277e5d7-eeaf-4534-b2fa-d2d90c787608)


# Penjelasan Kode
**Fungsi caesar_decrypt:**
- Fungsi ini menerima ciphertext dan shift sebagai parameter.
- Untuk setiap karakter dalam ciphertext, jika karakter tersebut adalah huruf, maka karakter tersebut akan digeser mundur sebanyak shift posisi.
- Jika karakter adalah huruf kecil, digunakan rumus chr((ord(char) - shift_amount - 97) % 26 + 97).
- Jika karakter adalah huruf besar, digunakan rumus chr((ord(char) - shift_amount - 65) % 26 + 65).
- Jika karakter bukan huruf, karakter tersebut ditambahkan ke hasil tanpa perubahan.

**Fungsi caesar_decrypt dipanggil dengan shift 9.**
- Hasil dekripsi dicetak.

**Jika Anda menjalankan kode di atas, hasil dekripsi akan menjadi:**
```
CRYPTOGRAPHY IS AN INDISPENSABLE TOOL FOR PROTECTING INFORMATION IN COMPUTING SYSTEMS IT IS USED EVERYWHERE BY BILLIONS OF PEOPLE WORLDWIDE ON A DAILY BASIS SECURING BOTH DATA AT REST AND DATA IN MOTION CRYPTOGRAPHIC SYSTEMS ARE FUNDAMENTAL TO STANDARD PROTOCOLS MOST NOTABLY THE TRANSPORT LAYER SECURITY TLS PROTOCOL WHICH ENABLES STRONG ENCRYPTION ACROSS A WIDER RANGE OF APPLICATIONS DESPITE ITS IMPORTANCE CRYPTOGRAPHY IS INHERENTLY FRAGILE EVEN THE MOST SECURE CRYPTOGRAPHIC SYSTEM CAN BE RENDERED COMPLETELY INSECURE BY A SINGLE SPECIFICATION FLAW OR PROGRAMMING ERROR TRADITIONAL SOFTWARE TESTING METHODS SUCH AS UNIT TESTING ARE INSUFFICIENT TO UNCOVER SECURITY VULNERABILITIES IN CRYPTO SYSTEMS INSTEAD CRYPTOGRAPHIC SECURITY IS ESTABLISHED THROUGH MATHEMATICAL MODELING AND RIGOROUS PROOFS DEMONSTRATING THAT A SYSTEM MEETS THE NECESSARY SECURITY PROPERTIES THESE ARGUMENTS OFTEN RELY ON PLAUSIBLE ASSUMPTIONS TO VALIDATE THEIR CLAIMS ONE OF THE EARLIEST AND SIMPLEST CRYPTOGRAPHIC TECHNIQUES IS THE CAESAR CIPHER WHICH DATES BACK TO AROUND BC THIS METHOD ENCODES PLAINTEXT BY SHIFTING EACH LETTER OF THE ALPHABET BY A FIXED NUMBER OF POSITIONS WHILE THIS APPROACH WAS EFFECTIVE AT THE TIME DUE TO THE OBSCURITY OF THE METHOD IT PROVIDES NO REAL SECURITY TODAY SINCE THERE ARE ONLY 25 POSSIBLE SHIFTS THE CIPHER CAN BE EASILY BROKEN THROUGH BRUTE FORCE DESPITE ITS SIMPLICITY THE CAESAR CIPHER REMAINS ONE OF THE MOST WIDELY RECOGNIZED ENCRYPTION TECHNIQUES HOWEVER IT OFFERS NO REAL PROTECTION AS IT CAN BE QUICKLY DECIPHERED BY HAND ADDITIONALLY ITS CIPHERTEXT IS EASILY IDENTIFIABLE BECAUSE THE FREQUENCY DISTRIBUTION OF LETTERS MIRRORS THAT OF THE ENGLISH LANGUAGE THIS HIGHLIGHTS A KEY PRINCIPLE IN MODERN CRYPTOGRAPHY TRUE SECURITY RELIES NOT ONLY ON SECRECY BUT ALSO ON STRONG MATHEMATICAL FOUNDATIONS AND COMPUTATIONAL INFEASIBILITY
```

# KESIMPULAN
| Kunci Enkripsi | Waktu Kriptanalisis yang Dibutuhkan | Perbandingan dengan Pendekatan Brute Force / Exhaustive Key Attack |
|----------------|-------------------------------------|---------------------------------------------------------------------|
| 9              | Sangat cepat (beberapa detik)      | Lebih efisien dibandingkan brute force, karena hanya perlu satu kunci |
|                |                                     | Brute force mencoba semua kemungkinan kunci (25 untuk Caesar)      |
