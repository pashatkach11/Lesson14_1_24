import string
import keyword


zminna_str = input()
zminna_bool = True

chisla = "0123456789"
veliki_literi = "A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z"
znaki_punktuacii = string.punctuation.replace("_", "")

if zminna_str[0] in chisla:
    zminna_bool = False

for i in range(len(zminna_str)):
    if zminna_str[i] == " ":
        zminna_bool = False
    if zminna_str[i] in veliki_literi:
        zminna_bool = False
    if zminna_str[i] in znaki_punktuacii:
        zminna_bool = False

print(zminna_bool)
