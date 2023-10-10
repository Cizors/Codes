NOTAS = []
CONTADOR = 0
MEDIA = 0

while CONTADOR < 3:
    NOTA = float(input(f"Digite a nota: "))

    NOTAS.append(NOTA)

    MEDIA = MEDIA + NOTAS[CONTADOR]

    CONTADOR += 1

MEDIAF = MEDIA / 3

if MEDIAF >= 7:
    print(f"Aprovado.")
elif 7 > MEDIAF >= 4:
    print(f"Reposição.")
else:
    print(f"Reprovado.")
