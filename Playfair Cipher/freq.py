from collections import Counter

# Baca ciphertext dari file txt
with open("cipher.txt", "r") as file:
    ciphertext = file.read().strip()

# Hitung frekuensi digram
digrams = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]
digram_freq = Counter(digrams)

# Urutkan berdasarkan frekuensi tertinggi
sorted_digrams = sorted(digram_freq.items(), key=lambda x: x[1], reverse=True)

# Simpan ke file
with open("digram_freq.txt", "w") as file:
    file.write("Frekuensi Digram (Paling Sering Muncul):\n")
    for digram, freq in sorted_digrams[:20]: 
        file.write(f"{digram}: {freq}\n")

print("Analisis frekuensi digram selesai. Hasil disimpan di 'digram_freq.txt'.")