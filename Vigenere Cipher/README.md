# VIGENERE CIPHER KRIPTANALYSIS

## LANGKAH-LANGKAH ANALISIS BESERTA PENJELASANNYA

1.  Membaca cipher text dari file dan menghapus whitespace
    
    ```python
    def read_ciphertext(filename):
    ```
    
2. Mencari pola berulang dalam ciphertext 
    
    ```python
    def find_repeating_sequences(ciphertext, min_length=3, max_length=12):
    ```
    
3. Menghitung jarak antar pola 
    
    ```python
    def calculate_distances(positions):
    ```
    
4. Menghitung faktor dari jarak 
    
    ```python
    def find_factors(number):
    ```
    
5. Menentukan panjang kunci yang paling mungkin berdasarkan faktor yang paling sering muncul
    
    ```python
    def count_factors(distances):
    ```
    
6. Mengelompokkan cipher text berdasarkan panjang kunci dan melakukan analisis frekuensi huruf
    
    ```python
    def group_by_key_position(ciphertext, key_length):
    
    def frequency_analysis(text):
    ```
    
7. Menebak kunci dengan membandingkan frekuensi huruf yang paling umun dalam bahasa inggris 
    
    ```python
    def find_likely_shift(cipher_group):
    ```
    
8. Menggunakan Kunci yang ditemukan untuk mendeskripsi ciphertext 
    
    ```python
    def guess_key(ciphertext, key_length):
    ```
    
9. Plaintext yang dihasilkan 
    
    ```
    CRYPTOGRAPHYPLAYSACRUCIALROLEINSAFEGUARDINGINFORMATIONWITHINCOMPUTINGSYSTEMSITISANINTEGRALPARTOFDAILYLIFEFORBILLIONSOFPEOPLEWORLDWIDEENSURINGTHESECURITYOFBOTHSTOREDANDTRANSMITTEDDATACRYPTOGRAPHICMECHANISMSUNDERPINESSENTIALPROTOCOLSPARTICULARLYTRANSPORTLAYERSECURITYTLSWHICHFACILITATESROBUSTENCRYPTIONACROSSNUMEROUSAPPLICATIONSHOWEVERDESPITEITSSIGNIFICANCECRYPTOGRAPHYISINHERENTLYDELICATEITSSECURITYCANBEENTIRELYCOMPROMISEDBYASINGLEDESIGNFLAWORCODINGMISTAKECONVENTIONALSOFTWARETESTINGAPPROACHESSUCHASUNITTESTINGAREINADEQUATEFORDETECTINGVULNERABILITIESINCRYPTOGRAPHICSYSTEMSINSTEADTHEIRSECURITYISVALIDATEDTHROUGHRIGOROUSMATHEMATICALANALYSISANDFORMALPROOFSDEMONSTRATINGADHERENCETOESSENTIALSECURITYPRINCIPLESTHESEPROOFSOFTENDEPENDONREASONABLEASSUMPTIONSTOSUBSTANTIATETHEIRCLAIMSONEOFTHEEARLIESTPOLYALPHABETICENCRYPTIONTECHNIQUESISTHEVIGENRECIPHERDEVELOPEDINTHETHCENTURYUNLIKESIMPLESUBSTITUTIONCIPHERSVIGENREENCRYPTIONEMPLOYSAREPEATINGKEYWORDTODETERMINELETTERSHIFTSMAKINGITMORERESISTANTTOFREQUENCYANALYSISFORCENTURIESITWASCONSIDEREDUNBREAKABLEDUETOITSCOMPLEXITYCOMPAREDTOMONOALPHABETICCIPHERSHOWEVERITISNOWEASILYDECIPHEREDUSINGTECHNIQUESSUCHASTHEKASISKIEXAMINATIONORFREQUENCYANALYSISOFREPEATINGPATTERNSINTHECIPHERTEXTDESPITEITSHISTORICALIMPORTANCETHEVIGENRECIPHERNOLONGERPROVIDESADEQUATESECURITYHIGHLIGHTINGAKEYPRINCIPLEINMODERNCRYPTOGRAPHYTRUEPROTECTIONRELIESNOTONLYONSECRECYBUTALSOONSTRONGMATHEMATICALFOUNDATIONSANDCOMPUTATIONALINFEASIBILITY
    ```

    Plaintext setelah dirapikan
    
    ```
    CRYPTOGRAPHY PLAYS A CRUCIAL ROLE IN SAFEGUARDING INFORMATION WITHIN COMPUTING SYSTEMS.
    It is an integral part of daily life for billions of people worldwide, ensuring the security of both stored and transmitted data.
    Cryptographic mechanisms underpin essential protocols, particularly Transport Layer Security (TLS), which facilitates robust encryption across numerous applications. However, despite its significance, cryptography is inherently delicate. Its security can be entirely compromised by a single design flaw or coding mistake.
    Conventional software testing approaches, such as unit testing, are inadequate for detecting vulnerabilities in cryptographic systems. Instead, their security is validated through rigorous mathematical analysis and formal proofs demonstrating adherence to essential security principles. These proofs often depend on reasonable assumptions to substantiate their claims.
    One of the earliest polyalphabetic encryption techniques is the **Vigenère cipher**, developed in the 16th century. Unlike simple substitution ciphers, Vigenère encryption employs a repeating keyword to determine letter shifts, making it more resistant to frequency analysis. For centuries, it was considered unbreakable due to its complexity compared to monoalphabetic ciphers.
    However, it is now easily deciphered using techniques such as the **Kasiski examination** or frequency analysis of repeating patterns in the ciphertext. Despite its historical importance, the Vigenère cipher no longer provides adequate security, highlighting a key principle in modern cryptography:
    True protection relies not only on secrecy but also on strong mathematical foundations and computational infeasibility.
    ```

## Ringkasan Hasil Analisis
1. Panjang kemungkinan kunci : 8
2. Kunci enkripsi : "SRIGALAK"
3. Tabel Subtitusi Huruf : 

| Posisi | Ciphertext | Kunci  | Pergeseran (A=0, ..., Z=25) | Plaintext |
|--------|-----------|--------|-----------------------------|-----------|
| 1      | U         | S      | -18                         | C         |
| 2      | I         | R      | -17                         | R         |
| 3      | G         | I      | -8                          | Y         |
| 4      | V         | G      | -6                          | P         |
| 5      | T         | A      | -0                          | T         |
| 6      | Z         | L      | -11                         | O         |
| 7      | G         | A      | -0                          | G         |
| 8      | B         | K      | -10                         | R         |
| 9      | S         | S      | -18                         | C         |
| 10     | G         | R      | -17                         | T         |
| 11     | P         | I      | -8                          | H         |
| 12     | E         | G      | -6                          | Y         |
| 13     | P         | A      | -0                          | P         |
| 14     | W         | L      | -11                         | L         |
| 15     | A         | A      | -0                          | A         |
| 16     | I         | K      | -10                         | Y         |

4. Waktu kriptanalisis : 1.92 detik 