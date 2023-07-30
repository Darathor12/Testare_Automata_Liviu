def adunare(*args):
    suma = 0

    for arg in args:
        suma = suma + arg

    return suma


print(adunare(1, 2, 3))

tuplu = (1, 2, 3)
print(adunare(*tuplu))
