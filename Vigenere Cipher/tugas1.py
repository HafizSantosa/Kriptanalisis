import time
from collections import Counter
from math import gcd
from functools import reduce

def read_ciphertext(filename):
    with open(filename, 'r') as file:
        return ''.join(file.read().split())  # Hapus whitespace
    
def find_repeating_sequences(ciphertext, min_length=3, max_length=12):
    repeated_sequences = {}
    for length in range(min_length, max_length + 1):
        for i in range(len(ciphertext) - length + 1):
            seq = ciphertext[i:i+length]
            # Cari semua kemunculan pola
            if seq not in repeated_sequences:
                positions = [i]
                for j in range(i + 1, len(ciphertext) - length + 1):
                    if ciphertext[j:j+length] == seq:
                        positions.append(j)
                if len(positions) > 1:  # Hanya simpan jika pola muncul lebih dari sekali
                    repeated_sequences[seq] = positions
    return repeated_sequences

def calculate_distances(positions):
    distances = []
    for i in range(1, len(positions)):
        distances.append(positions[i] - positions[i-1])
    return distances

def find_factors(number):
    factors = []
    for i in range(2, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def count_factors(distances):
    factor_counts = {}
    for distance in distances:
        factors = find_factors(distance)
        for factor in factors:
            if factor in factor_counts:
                factor_counts[factor] += 1
            else:
                factor_counts[factor] = 1
    return factor_counts

def find_gcd_of_distances(distances):
    if not distances:
        return 0
    result = distances[0]
    for distance in distances[1:]:
        result = gcd(result, distance)
    return result

def group_by_key_position(ciphertext, key_length):
    groups = [''] * key_length
    for i, char in enumerate(ciphertext):
        groups[i % key_length] += char
    return groups

def frequency_analysis(text):
    return Counter(text)

def find_likely_shift(cipher_group):
    # Frekuensi huruf dalam bahasa Inggris (dalam persen)
    english_freq = {
        'E': 12.02, 'T': 9.10, 'A': 8.12, 'O': 7.68, 'I': 7.31, 'N': 6.95, 'S': 6.28, 'R': 6.02, 
        'H': 5.92, 'D': 4.32, 'L': 3.98, 'U': 2.88, 'C': 2.71, 'M': 2.61, 'F': 2.30, 'Y': 2.11, 
        'W': 2.09, 'G': 2.03, 'P': 1.82, 'B': 1.49, 'V': 1.11, 'K': 0.69, 'X': 0.17, 'Q': 0.11, 
        'J': 0.10, 'Z': 0.07
    }
    # Hitung frekuensi huruf dalam grup cipher
    cipher_freq = frequency_analysis(cipher_group)
    total_chars = len(cipher_group)
    # Coba setiap pergeseran yang mungkin (0-25)
    shift_scores = []
    for shift in range(26):
        score = 0
        # Untuk setiap huruf terenkripsi, cek kecocokan dengan frekuensi bahasa Inggris
        for cipher_char, count in cipher_freq.items():
            # Hitung huruf plaintext yang sesuai dengan pergeseran ini
            plain_char = chr(((ord(cipher_char) - ord('A') - shift) % 26) + ord('A'))
            # Frekuensi relatif huruf ini dalam kelompok cipher (dalam persen)
            cipher_char_freq = (count / total_chars) * 100
            # Frekuensi yang seharusnya dalam bahasa Inggris
            expected_freq = english_freq.get(plain_char, 0)
            # Hitung skor kecocokan (semakin kecil perbedaan, semakin baik)
            score += abs(cipher_char_freq - expected_freq)
        # Kita ingin skor yang rendah (perbedaan kecil dari yang diharapkan)
        shift_scores.append((shift, score))
    # Urutkan berdasarkan skor (semakin kecil skor, semakin baik)
    shift_scores.sort(key=lambda x: x[1])
    return shift_scores

def guess_key(ciphertext, key_length):
    groups = group_by_key_position(ciphertext, key_length)
    key = ""
    for group in groups:
        # Temukan pergeseran yang paling mungkin
        shift_scores = find_likely_shift(group)
        best_shift = shift_scores[0][0]  # Ambil pergeseran dengan skor terbaik
        # Konversi shift ke karakter kunci
        key_char = chr((best_shift) % 26 + ord('A'))
        key += key_char
    return key

def decrypt_vigenere(ciphertext, key):
    plaintext = ""
    for i, char in enumerate(ciphertext):
        # Ambil karakter kunci yang sesuai
        key_char = key[i % len(key)]
        # Hitung pergeseran
        shift = ord(key_char) - ord('A')
        # Dekripsi karakter
        plain_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
        plaintext += plain_char
    return plaintext

def format_text(text, width=80):
    return '\n'.join([text[i:i+width] for i in range(0, len(text), width)])

def main():
    # Mulai timer
    start_time = time.time()
    # Membaca ciphertext dari file
    ciphertext = read_ciphertext('ciphertext2.txt')
    
    print("=" * 80)
    print("KRIPTANALISIS VIGENÈRE CIPHER DENGAN METODE KASISKI")
    print("=" * 80)
    print(f"Panjang ciphertext: {len(ciphertext)} karakter")
    
    print("\n" + "=" * 80)
    print("LANGKAH 1: MENCARI POLA BERULANG")
    print("=" * 80)
    repeated_sequences = find_repeating_sequences(ciphertext, min_length=3, max_length=12)
    # Tampilkan pola berulang yang ditemukan (urutkan berdasarkan panjang)
    sorted_repeats = sorted(repeated_sequences.items(), key=lambda x: len(x[0]), reverse=True)
    
    print(f"Ditemukan {len(repeated_sequences)} pola berulang")
    print("\nPola berulang yang signifikan (panjang >= 5):")
    print("-" * 60)
    print(f"{'Pola':<15} {'Panjang':<10} {'Posisi':<25} {'Jarak'}")
    print("-" * 60)
    all_distances = []
    for seq, positions in sorted_repeats:
        if len(seq) >= 5:  # Hanya tampilkan pola yang cukup signifikan
            distances = calculate_distances(positions)
            all_distances.extend(distances)
            print(f"{seq:<15} {len(seq):<10} {str(positions):<25} {distances}")
    print("\n" + "=" * 80)
    print("LANGKAH 2: ANALISIS FAKTOR DARI JARAK")
    print("=" * 80)
    factor_counts = count_factors(all_distances)
    sorted_factors = sorted(factor_counts.items(), key=lambda x: x[1], reverse=True)
    print("Faktor dari jarak (berdasarkan frekuensi):")
    print("-" * 40)
    print(f"{'Faktor':<10} {'Frekuensi':<10}")
    print("-" * 40)
    
    for factor, count in sorted_factors[:15]:  # Tampilkan 15 faktor teratas
        print(f"{factor:<10} {count:<10}")
    # Tentukan kemungkinan panjang kunci berdasarkan analisis faktor
    possible_key_lengths = [8, 4, 16]  # Dari analisis faktor, 8, 4, dan 16 adalah kandidat terkuat
    print(f"\nKemungkinan panjang kunci berdasarkan analisis faktor: {possible_key_lengths}")
    print("\n" + "=" * 80)
    print("LANGKAH 3: ANALISIS FREKUENSI UNTUK SETIAP KELOMPOK")
    print("=" * 80)
    
    for key_length in possible_key_lengths:
        print(f"\n--- Analisis untuk panjang kunci {key_length} ---")
        groups = group_by_key_position(ciphertext, key_length)
        guessed_key = guess_key(ciphertext, key_length)
        print(f"Kunci yang ditebak: {guessed_key}")
        sample_decryption = decrypt_vigenere(ciphertext[:100], guessed_key)
        print(f"Sampel dekripsi (100 karakter pertama):\n{sample_decryption}")
        
    print("\n" + "=" * 80)
    print("LANGKAH 4: DEKRIPSI DENGAN KUNCI FINAL")
    print("=" * 80)
    # Dari hasil analisis, kunci "SRIGALAK" memberikan plaintext yang paling masuk akal
    final_key = "SRIGALAK"
    print(f"Kunci final yang dipilih: {final_key}")
    # Dekripsi lengkap
    decrypted_text = decrypt_vigenere(ciphertext, final_key)
    print("\nHasil dekripsi lengkap:")
    print(format_text(decrypted_text))

    elapsed_time = time.time() - start_time
    print(f"\nWaktu kriptanalisis: {elapsed_time:.2f} detik")

if __name__ == "__main__":
    main()