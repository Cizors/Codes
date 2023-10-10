print(f"[Bem Vindo ao Conversor de Temperaturas]")
print(f"")

while True:
    print(f"[1 - Converter de Celsius para Fahrenheit]")
    print(f"[2 - Converter de Fahrenheit para Celsius]")

    ESCOLHA = int(input("Opção: "))
    print(f"")

    match int(ESCOLHA):
        case 1:
            CELSIUS = float(input("Digite a temperatura em Celsius: "))
            print(f"")
            RESULT1 = (CELSIUS * 9/5) + 32
            print(f"{CELSIUS} graus Celsius é igual a {RESULT1} graus Fahrenheit.")
            print(f"")
        case 2:
            FAHRENHEIT = float(input("Digite a temperatura em Fahrenheit: "))
            print(f"")
            RESULT2 = (FAHRENHEIT - 32) * 5/9
            print(f"{FAHRENHEIT} graus Fahrenheit é igual a {RESULT2} graus Celsius.")
            print(f"")

    RESPOSTA = input("Deseja realizar outra conversão [S/N]: ").upper()

    if RESPOSTA == 'S':
        continue
    elif RESPOSTA == 'N':
        break
    else:
        print(f"Resposta Inválida, encerrando.")
        break

