# Fitimi i 16 subkey per secilin round te algoritmit DES

# Ky eshte kodi gjeneral per implementimin e nje PBox
# n paraqet numrin e input bitave
# P eshte nje liste qe permban m integera
# Integerat ne P jane ne mes te 1 dhe n
# Input parametri x eshte nje integer n-bitesh
# Outputi y eshte nje integer m-bitesh
def pbox(x, P, n):
    y = 0
    for i in P:
        y <<= 1
        y ^= (x >> (n-i)) & 1
    return y

# PBoxat qe perdoren ne key schedule jane PC1, PC2, RHL1 dhe RHL2

# Permuted Choice One
# B64 ne B56
PC1 = [57, 49, 41, 33, 25, 17, 9, 1,
       58, 50, 42, 34, 26, 18, 10, 2,
       59, 51, 43, 35, 27, 19, 11, 3,
       60, 52, 44, 36, 63, 55, 47, 39,
       31, 23, 15, 7, 62, 54, 46, 38,
       30, 22, 14, 6, 61, 53, 45, 37,
       29, 21, 13, 5, 28, 20, 12, 4]


# Permuted Choice Two
# B56 ne B48
PC2 = [14, 17, 11, 24, 1, 5, 3, 28,
       15, 6, 21, 10, 23, 19, 12, 4,
       26, 8, 16, 7, 27, 20, 13, 2,
       41, 52, 31, 37, 47, 55, 30, 40,
       51, 45, 33, 48, 44, 49, 39, 56,
       34, 53, 46, 42, 50, 36, 29, 32]
