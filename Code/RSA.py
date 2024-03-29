# already given
#c=cipherText
c=421345306292040663864066688931456845278496274597031632020995583473619804626233684
#n=modulus
n=631371953793368771804570727896887140714495090919073481680274581226742748040342637
#public exponent
e=65537


# Find factors of the modulus using - https://www.dcode.fr/prime-factors-decomposition
p = 1461849912200000206276283741896701133693
q = 431899300006243611356963607089521499045809

# compute 
# Calculate Euler's totient function phi(n)
phi_n = (p-1)*(q-1)

# Compute the private exponent d using the public exponent e and phi(n)
d = pow(e, -1, phi_n)

# Decrypt the ciphertext c using the private exponent d and modulus n
plaintext = pow(c,d,n)

# decodes the hex values of the plaintext
print(bytearray.fromhex(hex(plaintext)[2:]).decode())