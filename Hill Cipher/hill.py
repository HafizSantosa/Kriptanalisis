import numpy as np
from sympy import Matrix

def text_to_num(text):
    return [ord(c.upper()) - ord('A') for c in text if c.isalpha()]

def num_to_text(nums):
    return ''.join([chr(n + ord('A')) for n in nums])

# Matriks invers kunci yang sudah ditemukan
key_inv = np.array([
    [8, 21, 21],
    [5, 8, 12],
    [10, 21, 8]
])

def decrypt_hill(ciphertext, key_inv):
    n = key_inv.shape[0]
    cipher_num = text_to_num(ciphertext)
    plain_num = []
    
    # Padding jika perlu
    if len(cipher_num) % n != 0:
        cipher_num += [0] * (n - len(cipher_num) % n)
    
    # Dekripsi per blok
    for i in range(0, len(cipher_num), n):
        block = cipher_num[i:i+n]
        decrypted_block = np.dot(key_inv, block) % 26
        plain_num.extend(decrypted_block)
    
    return num_to_text(plain_num)

# Ciphertext lengkap
ciphertext = "CDECCZDKQFYRYRWYWKKVTSBQABTRVRITRXVVKWKJKEMUEVKLYUPUAFSPPSFSKZVGJKKNLWNFXSMUDVHKSWMFERVUWEVZTZQVOGWALCAYTKXAKNKYDZMTWATADALYSANZSBMIGPUGNTWHEJRSKSTLQKFRXAKHMOHEYODUMSFTAMOBSKBFWZKGZEVAKSHQHPGJUKKLNSZAIFCMUKUKWMUUDVVOWHWXEAVWODIAMOBSDNNNUYYRVRWMPQPYJDZRXDZBUUKOPUXIZQTHSKKHEYATYCONMHOACPMNIESNKZZYBKTZHXCGOABREJCIDCJCRVRWNFCJPCIWYNQGCGSLDWLLCHBWNFLCMGNNTDLMPTLSYFWAUMGWFMWQCCWPLAMTSZXAULMDEADALPBQIDUTSJGSWPGKBIAMOSOKSFGFBDDLMECGVUDVEEZYCORCJEIOMXENEQUMGZHUUSOSCNSFSMDPALWXAHIDENWFJOQJILLELRNAUVQQQUINZIKVMSSSGMGRHSKZWJVQQASVCKVIZGIQWPIQGJKLWURYLIQBOAZMHOACPMNIESNCUKXWSGYEBHTYIBELMHOACPMNIESNSKKHEYOOPTSOFRFHSGBZHXCXATDOOFNOEWKQXHJYCUYUZBPXSMDESDDZGANUGMFWSMMLMCYZEVECXLFNUACWPVMHOBSWQCQWROHPVUMDOTEMXBGDANZKNUCSLFSKPCJUGAURCOQZQUEXTFWNFFPPUPLZMTAVZQQZCJCRVRWNFYILHSXUSQBXBNSIFSFCWPHAVOHVWCRTNPIVQWLYTEEEQXEMXBUPCAFBXBPGMPGVTPDIDINGOCPMPUYXHWVZNWDMZGOZDGQHSGWAQXLZGPGSYUZAPVSBQBXBPGMPGVTPDVGGAWQOPAAVZDSSNLJANNSETBGXSSBFCJDMLCHBWNFMULCJCRVRNNJIUIFFVBVLHYCKKSTRZPQICAQUUPEKMEYLECLAHACASRIADDUVDHIQWZATORLZMCAIEOMJNGONEOVCCOGXQMPXHJYCUVUZJOQDTJMXFWQCEQXQJOMJPOJIABTRVRPUVEDSDDHSUOFIUTQJFE5FWGATDZQVZVHBHZAPVSBQCBOXUNFQGZZPKSQQDUWUTGYNXLXFYEVZAYRFLAMDUNZUMPVDZZDMETGIVHMDNHXAXPLINCAYNSVDNAXSMVVLYDTCRPLRFLAMTSZXAULWDHCVAKKOHPVUMKJOSQGQBWYKLKRQSKKMMJLWWWCYKEUGNWBGKNLMUTRYYYBLOTDNWREQXACLBEVUDVDECEQXMFWFRFUMONGIENMOEY"

# Dekripsi lengkap
plaintext = decrypt_hill(ciphertext, key_inv)
print(plaintext)
