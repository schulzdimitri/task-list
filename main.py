# from src.task import task


def add_task(task_name: str, task_list: list):
    task_list.append({"task_name": task_name, "completed": False, "id": len(task_list)})
    
    print(f"Tarefa '{task_name}' adicionada com sucesso!")
    
    
def show_tasks(task_list: list):
    for index, task in enumerate(task_list, start=1):
        status = "✅" if task['completed'] else "⏹️ "
        print(f"{status} {index} - {task['task_name']}")
    

def update_task(task_list: list, new_name: str, task_id: int):
    index = task_id - 1
    last_name = task_list[index]['task_name']
    
    task_list[index]['task_name'] = new_name
    print(f"Tarefa Renomeada de '{last_name}' para '{new_name}'")


def complete_task(task_list: list, task_id: int):
    index = task_id - 1
    task_list[index]['completed'] = True
    
    print('Tarefa completada com sucesso!')
    show_tasks(task_list)


def remove_completed_tasks(task_list: list):
    for task in task_list:
        if task['completed']:
            task_list.remove(task)
    print('Tarefas concluidas removidas com sucesso!')


def main():
    task_list = []
    
    print("\n Menu do Gerenciador de Tarefas \n")
    print("1 - Adicionar Tarefa")
    print("2 - Ver Tarefas")
    print("3 - Atualizar Tarefa")
    print("4 - Completar Tarefa")
    print("5 - Deletar tarefas concluídas")
    print("6 - Sair")
    
    while True:
        try:
            choice = int(input("Digite a opção desejada: "))
        except:
            print('Valor inválido. Tente inserir um número.')
            continue
        
        match choice:
            case 1:
                task_name = input("Digite o nome da tarefa: ")
                add_task(task_name, task_list)
                
            case 2:
                show_tasks(task_list)
                
            case 3:
                show_tasks(task_list)
                try:
                    task_id = int(input('Digite o numero da tarefa que deseja alterar: ')) 
                except:
                    print('Valor inválido. Tente inserir um número.')
                    continue
                
                new_task_name = input('Novo nome: ')
                update_task(task_list, new_task_name, task_id)
            
            case 4:
                show_tasks(task_list)
                try:
                    task_id = int(input('Número da tarefa que deseja completar: '))
                except:
                    print('Valor inválido. Tente inserir um número.')
                    continue
                complete_task(task_list, task_id)
                
            case 5:
                remove_completed_tasks(task_list)
                
            case 6:
                print("Saindo do Gerenciador de Tarefas...")
                return
            
            case _:
                print("Opção inválida. Tente novamente.")
                
    
if __name__ == "__main__":
    main()