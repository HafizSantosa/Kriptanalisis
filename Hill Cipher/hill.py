import numpy as np
from sympy import Matrix, mod_inverse
import re

def text_to_numbers(text):
    # Remove non-alphabetic characters and convert to uppercase
    text = re.sub(r'[^A-Za-z]', '', text).upper()
    # Convert to numbers (A=0, B=1, ..., Z=25)
    return [ord(char) - ord('A') for char in text]

def numbers_to_text(numbers):
    # Convert numbers back to text
    return ''.join([chr(num + ord('A')) for num in numbers])

def matrix_mod_inverse(matrix, modulus):
    # Calculate the modular multiplicative inverse of a matrix
    det = int(np.round(np.linalg.det(matrix))) % modulus
    det_inverse = mod_inverse(det, modulus)
    
    # Adjugate matrix
    if len(matrix) == 2:
        adjugate = np.array([[matrix[1, 1], -matrix[0, 1]], 
                            [-matrix[1, 0], matrix[0, 0]]])
    else:  # For 3x3 matrix
        adjugate = np.zeros((3, 3), dtype=int)
        for i in range(3):
            for j in range(3):
                minor = np.delete(np.delete(matrix, i, axis=0), j, axis=1)
                adjugate[j, i] = int(np.round(np.linalg.det(minor))) * (-1)**(i+j)
    
    # Multiply adjugate by det_inverse and take modulo
    inverse = (adjugate * det_inverse) % modulus
    return inverse

def hill_decrypt(ciphertext_numbers, key_matrix, matrix_size, modulus=26):
    # Ensure the ciphertext length is a multiple of matrix_size
    if len(ciphertext_numbers) % matrix_size != 0:
        ciphertext_numbers += [0] * (matrix_size - len(ciphertext_numbers) % matrix_size)
    
    # Initialize plaintext
    plaintext_numbers = []
    
    # Process in blocks of matrix_size
    for i in range(0, len(ciphertext_numbers), matrix_size):
        block = ciphertext_numbers[i:i+matrix_size]
        result = np.dot(key_matrix, block) % modulus
        plaintext_numbers.extend(result.tolist())
    
    return plaintext_numbers

def hill_known_plaintext_attack(plaintext, ciphertext, matrix_size=2, modulus=26):
    """
    Perform a known-plaintext attack on Hill cipher
    
    Args:
        plaintext: Known plaintext string
        ciphertext: Corresponding ciphertext string
        matrix_size: Size of the Hill cipher matrix (2 for 2x2, 3 for 3x3)
        modulus: Modulus for the cipher (26 for standard English alphabet)
        
    Returns:
        Encryption key matrix and its inverse (decryption key)
    """
    # Convert texts to number sequences
    p_nums = text_to_numbers(plaintext)
    c_nums = text_to_numbers(ciphertext)
    
    # Ensure we have enough plaintext-ciphertext pairs
    if len(p_nums) < matrix_size * matrix_size or len(c_nums) < matrix_size * matrix_size:
        raise ValueError("Not enough plaintext-ciphertext pairs for the given matrix size")
    
    # Create matrices for the first matrix_size^2 characters
    P = np.zeros((matrix_size, matrix_size), dtype=int)
    C = np.zeros((matrix_size, matrix_size), dtype=int)
    
    # Fill the matrices
    for i in range(matrix_size):
        for j in range(matrix_size):
            idx = i * matrix_size + j
            P[i, j] = p_nums[idx]
            C[i, j] = c_nums[idx]
    
    # Check if plaintext matrix is invertible
    try:
        p_det = int(np.round(np.linalg.det(P))) % modulus
        # Check if determinant is coprime with modulus
        if np.gcd(p_det, modulus) != 1:
            raise ValueError("Plaintext matrix is not invertible mod 26. Try another segment.")
    except:
        raise ValueError("Plaintext matrix is not invertible. Try another segment.")
    
    # Calculate P^-1
    P_inv = matrix_mod_inverse(P, modulus)
    
    # Calculate key matrix K = C * P^-1
    K = (np.dot(C, P_inv)) % modulus
    
    # Calculate decryption key K^-1
    K_inv = matrix_mod_inverse(K, modulus)
    
    return K, K_inv

# Known plaintext and corresponding ciphertext
plaintext = "HELLOCYBERFOXATTACKERHERE"
ciphertext = "CDECCZDKQFYRYRWYWXKVTSBQ"  # First 24 characters of the ciphertext

# Try with 2x2 matrix first
matrix_size = 2
try:
    # Find encryption and decryption keys
    encryption_key, decryption_key = hill_known_plaintext_attack(plaintext, ciphertext, matrix_size)
    print(f"Using {matrix_size}x{matrix_size} matrix:")
    print(f"Encryption Key:\n{encryption_key}")
    print(f"Decryption Key:\n{decryption_key}")
    
    # Test decryption on a small segment to verify
    test_cipher = text_to_numbers(ciphertext[:10])
    test_plain = hill_decrypt(test_cipher, decryption_key, matrix_size)
    print(f"Test Decryption: {numbers_to_text(test_plain)}")
    
except ValueError as e:
    print(f"Error with {matrix_size}x{matrix_size} matrix: {e}")
    # If 2x2 fails, try 3x3
    matrix_size = 3
    try:
        encryption_key, decryption_key = hill_known_plaintext_attack(plaintext, ciphertext, matrix_size)
        print(f"\nUsing {matrix_size}x{matrix_size} matrix:")
        print(f"Encryption Key:\n{encryption_key}")
        print(f"Decryption Key:\n{decryption_key}")
        
        # Test decryption
        test_cipher = text_to_numbers(ciphertext[:15])
        test_plain = hill_decrypt(test_cipher, decryption_key, matrix_size)
        print(f"Test Decryption: {numbers_to_text(test_plain)}")
    except ValueError as e:
        print(f"Error with {matrix_size}x{matrix_size} matrix: {e}")
        print("Try another segment of plaintext-ciphertext or different matrix size.")

# Now let's decrypt the full ciphertext
full_ciphertext = """
CDECCZDKQFYRYRWYWXKVTSBQABTRVRITRXVVKWKJKEMUEVKLYUPUAFSPPSFSKZ
VGJKKNLWNFXSMUDVHKSWMFERVUWEVZTZQVOGWALCAYTKXAKNKYDTZMTWATADAL
YSANZSBMIGPUGNTMHFJRSKSTLQKFRXAKHMOHEYQDUMSFIAMOBSKBFWZKGZEVAK
SHQHPGJUKKLNSZAIFCWUKUKWMMJUDVVOWHWXEAVWODIAMOBSDNNNUYYRVRWMPQ
PYJDZRXDZBJUKOPUXIZQTHSKKHEYATYCONMHOACPMNIESNKZZYBKTZHXCGOABR
EJCIDCJCRVRWNFCJPCUWYNQGCGSLJDWLCHBWNFLCMGNNTDLMPTLSYFWAUMGWFM
WQCCWPLAMTSZXAULWDEADALPBQIDUTSJGSWPGKBIAMOBSOKSPGFBDDLMECGVUD
VEEZYCORCJEIOMXENEQUMGZHUUSOSCNSFSMDPALWXAHIDEWNFJOQJLLELRNAUV
OQQDUINZIKVMSSSGOMGRHSKZWJVOQASVCKVIZGIQWPIQGJKLWURYLIQBOAZMHO
ACPMNIESNCUKXWSGIYEBHTYIBEIMHOACPMNIESNSKKHEYOOPTSOFRFHSGBZHXC
XATDOOFNOEWKQXHJYCUYUZBPXSMDESDJDOZGANUGMFWSMMLMCYZEVECXLFNUAC
WPYMHOBSWQCQWROHPVUMDOTEMXBGDANZKNUCSLFSKPCJUGAURCOQZOUEXTFWNF
ETPUPLZMTAVZQOZCJCRVRWNFYILHSXUSQBXBNSIFSFCWPHAVOHVWCRTNPIWQWL
YTEEEQXEMXBUPCAFBXBPGMPGVTFDTDLNGOCPMPUYXHWVZNMVDMZGOZDGQHSGWA
QXLZGPGSYUZAPVSBQBXBPGMPGVTFDVGGAWQOPAAVZDSSNLJANNSETBGXSSBFCJ
DWLCHBWNFMULCJCRVRNWJIUIFFVBVLHYCKKSTRZPQICAQUUPEKMEYLECLAHACA
SRIADDUVDHIQWZAIORLZMCAIEOMJNGONEDVCCOGXQMPXHJYCUYUZJOQDTJMXFW
QCEQXQJOMJPOJIABTRVRPUYEDSDDHSUOFIUTQJFESFWGATDZQVZVHBHZAPVSBQ
CBOXUNFQGZZPKSQQDUWUTGYNXLXFYEVZAYRFLAMDUNZUMPVDZZDMETGIVHMDNH
XAXPLLNCAYNSVDNAXSMVVLYDTCRPLRFLAMTSZXAULWDHCVAKKOHPVUMKJOSQGQ
BWYKLKRQSKKMMJLWWWTCYKEUGNWBGKNLWUTRYYYBLOIDNWREQXACLBEVUDVDEC
EQXMFWFRFUMONGIENMOEY
"""
# Clean and convert to numbers
full_ciphertext = re.sub(r'\s+', '', full_ciphertext)
cipher_nums = text_to_numbers(full_ciphertext)

# Decrypt the full text
try:
    plaintext_nums = hill_decrypt(cipher_nums, decryption_key, matrix_size)
    decrypted_text = numbers_to_text(plaintext_nums)
    print("\nFull Decrypted Text:")
    
    # Print in readable chunks
    chunk_size = 50
    for i in range(0, len(decrypted_text), chunk_size):
        print(decrypted_text[i:i+chunk_size])
except Exception as e:
    print(f"Error decrypting full text: {e}")