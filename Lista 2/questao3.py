print(f"[ Operações - Adição ]")

while True:
    NUM1 = float(input("Digite um número: "))
    NUM2 = float(input("Digite outro número: "))
    print(f"")

    RESULT = NUM1 + NUM2

    print(f"{NUM1} + {NUM2} = {RESULT}")
    print(f"")

    print(f"Deseja realizar mais uma soma? [S / N]")
    ANSWER = input("Resposta: ").lower()
    print(f"")

    if ANSWER == 'n':
        break
    elif ANSWER != 's':
        print(f"Resposta Inválida")
        break
