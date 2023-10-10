grade1 = float(input("Digite a primeira nota: "))
grade2 = float(input("Digite a segunda nota: "))

average = (grade1 + grade2) / 2

if average == 10:
    print(f"Aprovado com Distinção")
elif average >= 7:
    print(f"Aprovado")
else:
    print(f"Reprovado")
