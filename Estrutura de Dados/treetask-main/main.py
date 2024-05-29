import os
from Relacionamento import Relacionamento

def exibir_menu():
    print("\n===== [MENU] =====")
    print("1. Inserir usuário")
    print("2. Remover usuário")
    print("3. Visualizar Relacionamentos")
    print("4. Adicionar Relacionamento")
    print("5. Encontrar Usuário")
    print("6. Encontrar Comunidade")
    print("0. Sair")
    print("==================")

def main():
    relacionamento = Relacionamento()
    
    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            usuario_id = input("Digite o ID do novo usuário: ")
            nome = input("Digite o nome do novo usuário: ")
            relacionamento.adicionar_usuario(usuario_id, nome)
            print("")
            input("Pressione enter para continuar...")
            os.system("cls" if os.name == "nt" else "clear")
        elif escolha == '2':
            usuario_id = input("Digite o ID do usuário a ser removido: ")
            relacionamento.remover_usuario(usuario_id)
            print("")
            input("Pressione enter para continuar...")
            os.system("cls" if os.name == "nt" else "clear")
        elif escolha == '3':
            print("Estrutura de relacionamentos:")
            relacionamento.mostrar_arvore()
            print("")
            input("Pressione enter para continuar...")
            os.system("cls" if os.name == "nt" else "clear")
        elif escolha == '4':
            usuario_id1 = input("Digite o ID do primeiro usuário: ")
            usuario_id2 = input("Digite o ID do segundo usuário: ")
            relacionamento.adicionar_relacionamento(usuario_id1, usuario_id2)
            input("Pressione enter para continuar...")
            os.system("cls" if os.name == "nt" else "clear")
        elif escolha == '5':
            usuario_id = input("Digite o ID do usuário a ser encontrado: ")
            usuario = relacionamento.encontrar_usuario(usuario_id)
            if usuario:
                print(f"Usuário encontrado: {usuario.nome} ({usuario.usuario_id})")
            print("")
            input("Pressione enter para continuar...")
            os.system("cls" if os.name == "nt" else "clear")
        elif escolha == '6':
            comunidades = relacionamento.encontrar_comunidades()
            for idx, comunidade in enumerate(comunidades):
                print(f"Comunidade {idx + 1}:")
                for usuario in comunidade:
                    print(f"{usuario.nome} ({usuario.usuario_id})")
            print("")
            input("Pressione enter para continuar...")
            os.system("cls" if os.name == "nt" else "clear")
        elif escolha == '0':
            print("Saindo...")
            break
        else:
            print("Opção incorreta. Por favor, escolha novamente.")
            input("Pressione enter para continuar...")
            os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    main()