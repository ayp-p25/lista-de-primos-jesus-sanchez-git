Lim = int(input("Ingresa el limite de la lista : \n"))
def es_primo(N):
    P = True
    i = 2
    while i < N:
        if N % i == 0:
            P = False
            break
        i += 1
    else :
        P = True
    return P
L = []
N = 2
while N <= Lim:
    if es_primo(N):
        L.append(N)
    N += 1
print(L)