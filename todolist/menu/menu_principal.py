from db.task_db import insert_task, update_task, delete_task, list_tasks, search_task

def menu(user):
    while True:
        print(f'Bem vindo {user[1]}')
        print("1 - Cadastrar Tarefa\n2 - Atualizar Tarefa\n3 - Deletar\n4 - Listar Tarefas\n5 - Buscar Tarefa")
        opc = input("Digite a opc: ")

        if opc == '1':
            title = input("Digite o titulo: ")
            insert_task(title, user[0])
        elif opc == '2':
            title = input("Digite o novo titulo: ")
            task_id = int(input('Digite o id da task: '))
            update_task(title, task_id, user[0])
        elif opc == '3':
            task_id = int(input('Digite o id da task: '))
            delete_task(task_id, user[0])
        elif opc == '4':
            tasks = list_tasks(user[0])
            for task in tasks:
                print(task[1])
        elif opc == '5':   
            title = input("Pesquisar por: ")
            tasks = search_task(title)
            print(tasks)