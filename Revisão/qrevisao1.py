PARES = []
IMPARES = []
RESULTADO = 0
CONTADOR = 1

NUMERO = int(input("Digite um valor inteiro: "))
print(f"")
          
while CONTADOR <= NUMERO:

    RESULTADO = CONTADOR % 2

    if RESULTADO == 0:
        PARES.append(CONTADOR)
    else:
        IMPARES.append(CONTADOR)

    CONTADOR += 1

print(f"Números Pares até {NUMERO}: {PARES}")
print(f"Números Primos até {NUMERO}: {IMPARES}")
