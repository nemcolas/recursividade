'''primeiro ver qual o criterio de parada da recursividade'''

def potencia(base, exp):
    if exp == 0: # criterio de parada
        return 1 # se o expoente for 0, o resultado é 1
    else: 
        return base * potencia (base, exp-1) # se o expoente for diferente de 0, a base é multiplicada por ela mesma, e o expoente é decrementado em 1
    


base = int(input("Digite a base: "))

exp = int(input("Digite o expoente: "))

print(potencia(base, exp))




    