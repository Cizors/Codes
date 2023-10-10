print(f"[      Registro      ]")
print(f"")

CONTADOR = 0
IDADE = 0
SALARIO = 0
SEXO = 'a'
ESTADO_CIVIL = "a"

while CONTADOR <= 3:
    NOME = str(input("Digite um nome: "))
    CONTADOR = len(NOME)

while IDADE <= 0 and IDADE < 150:
    IDADE = int(input("Digite uma idade: "))

while SALARIO <= 0:
    SALARIO = int(input("Digite um salário: "))

while SEXO not in ['F', 'M']:
    print(f"")
    print(f"[F - Feminino]")
    print(f"[M - Masculino]")
    SEXO = input("Digite: ").upper()

while ESTADO_CIVIL not in ['S', 'C', 'V', 'D']:
    print(f"")
    print(f"[S - Solteiro(a)]")
    print(f"[C - Casado(a)]")
    print(f"[V - Viúvo(a)]")
    print(f"[D - Divorciado(a)]")
    ESTADO_CIVIL = input("Digite: ").upper()

print(f"")
print(f"[      Registro      ]")
print(f"Nome: {NOME}")
print(f"Idade: {IDADE}")
print(f"Salário: {SALARIO}")
print(f"Sexo: {SEXO}")
print(f"Estado Civil: {ESTADO_CIVIL}")
print(f"[--------------------]")
