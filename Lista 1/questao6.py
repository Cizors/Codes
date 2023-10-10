print(f"Em qual turno você estuda?")
print(f"M - Matutino")
print(f"V - Vespertino")
print(f"N - Noturno")

answer = input("Digite: ")

match answer.lower():
    case "m":
        print(f"Bom Dia!")
    case "v":
        print(f"Boa Tarde!")
    case "n":
        print(f"Boa Noite!")
    case _:
        print(f"Valor Inválido!")
