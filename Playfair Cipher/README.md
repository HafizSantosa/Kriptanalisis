# Penjelasan Kode

Pertama-tama, ciphertext yang tersimpan dalam cipher.txt dibuat menjadi pasangan huruf pada kode `digraph.py` dan hasilnya disimpan pada `digraphs.txt`.

Kemudian, pasangan kode tersebut dihitung frekuensi kemunculannya pada kode `freq.py` yang hasilnya disimpan di `digram_freq.txt`.

Setelah itu melakukan dekripsi ciphertext di `decrypt.py` dengan key matrix disimpan pada `key_matrix.txt` dan hasil dekripsinya disimpan di `plaintext.txt`. Tetapi setelah berkali-kali mencoba key yang berbeda, tidak dapat mendekripsikan ciphertext secara lengkap. Dengan menggunakan key "CRYPTOGRAPHY", didapatkan ciphertext bisa terdekripsi sebagian. Ditemukan beberapa kata dalam bahasa Inggris seperti 'Fill', 'Be', 'My', 'Head'.
