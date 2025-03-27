import time
import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def brute_force_affine(P1, C1, P2, C2, n=256):
    """Mencari m dan b dengan brute force"""
    start_time = time.time() 
    
    for m in range(n):  
        if gcd(m, n) != 1:
            continue

        for b in range(n):  
            if (m * P1 + b) % n == C1 and (m * P2 + b) % n == C2:
                end_time = time.time()  
                return m, b, end_time - start_time 

    end_time = time.time()  
    return None, None, end_time - start_time  

P1, C1 = 0xFF, 0xB7
P2, C2 = 0xD8, 0x32

m, b, execution_time = brute_force_affine(P1, C1, P2, C2)

if m is not None:
    print(f"Ditemukan: m = {m}, b = {b}, Waktu Eksekusi = {execution_time:.6f} detik")
else:
    print(f"Tidak ditemukan pasangan yang cocok. Waktu Eksekusi = {execution_time:.6f} detik")
