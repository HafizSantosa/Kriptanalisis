import time

def decrypt_affine(C1, C2, P1, P2, n=256):
    start_time = time.time()  # Mulai timer
    
    # Mencari m menggunakan invers modulo
    delta_C = (C1 - C2) % n
    delta_P = (P1 - P2) % n
    m = (delta_C * pow(delta_P, -1, n)) % n  # Menggunakan invers modulo

    # Mencari b
    b = (C1 - m * P1) % n

    end_time = time.time()  # Selesai timer
    elapsed_time = end_time - start_time
    
    print(f"Nilai m: {m}, Nilai b: {b}")
    print(f"Waktu kriptanalisis: {elapsed_time:.6f} detik")

# Contoh input
P1, C1 = 0xFF, 0xB7
P2, C2 = 0xD8, 0x32

decrypt_affine(C1, C2, P1, P2)
