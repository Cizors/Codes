counter = 1

while counter < 5:
    password = str(input("Digite a senha: "))
    if password == "cesmac":
        print(f"Logado com Sucesso.")
        break
    elif counter == 3:
        print(f"Resta 1 tentativa.")
    elif counter == 4:
        print(f"Usuário Bloqueado.")
        break
    counter += 1
