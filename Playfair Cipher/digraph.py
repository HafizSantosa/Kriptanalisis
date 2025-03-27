def create(ciphertext):        
    # Membuat digraph (pasangan 2 huruf)
    digraphs = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]
    
    return digraphs

def read(filename):
    with open(filename, 'r') as file:
        ciphertext = file.read().replace('\n', '').replace(' ', '').upper()
    return ciphertext

def save(digraphs, filename):
    with open(filename, 'w') as file:
        for dg in digraphs:
            file.write(dg + '\n')

# File input dan output
input_file = 'cipher.txt'
output_file = 'digraphs.txt'

# Membaca ciphertext dari file
ciphertext = read(input_file)

# Membuat digraphs
digraphs = create(ciphertext)

# Menyimpan digraphs ke file
save(digraphs, output_file)
print(f"Digraphs telah disimpan ke {output_file}")

