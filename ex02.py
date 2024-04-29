
def somatorio(n):
    if n == 1:
        return 1
    else:
        return n + somatorio(n - 1)


numero = int(input('Digite um numero: '))
print(f'Somatorio: {somatorio(numero)}')