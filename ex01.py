#exemplo de calculo fatorial usando recursividade

def fatorial(n):
    if n == 1:
        return 1
    else:
        return n * fatorial(n-1)
    

n = int(input("Digite um número: "))
print(fatorial(n))