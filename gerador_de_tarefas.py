import random

with open('exemplo.txt', 'w') as f:
    letras = "abcdefghijklmnopqrstuvwxyz"
    for i in letras:
        for j in range(4):
            nome = f'{i}{j}'
            numero = random.randint(1, 45)
            f.write(f'{nome} {numero}\n')