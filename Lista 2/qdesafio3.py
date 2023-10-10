CONJUNTO = []
CONTADOR = 0

while True:
    NUMERO = -1
    while NUMERO < 0 or NUMERO > 1000:
        NUMERO = float(input("Digite um número: "))
    CONJUNTO.append(NUMERO)

    CONTADOR = len(CONJUNTO)

    if CONTADOR >= 2:
        print(f"")
        print(f"Deseja digitar outro número? [S / N]")
        RESPOSTA = input("Resposta: ").lower()
        
        if RESPOSTA == 'n':
            break
        elif RESPOSTA != 's':
            print(f"Resposta Inválida")
            break

CONJUNTO.sort()

RESULTADO = CONJUNTO[0] + CONJUNTO[CONTADOR - 1]

print(f"")
print(f"Menor Valor: {CONJUNTO[0]}")
print(f"Maior Valor: {CONJUNTO[CONTADOR - 1]}")
print(f"Soma dos Valores: {RESULTADO}")
