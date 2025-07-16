from src.task import task


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
                task.add_task(task_name, task_list)
                
            case 2:
                task.show_tasks(task_list)
                
            case 3:
                task.show_tasks(task_list)
                try:
                    task_id = int(input('Digite o numero da tarefa que deseja alterar: ')) 
                except:
                    print('Valor inválido. Tente inserir um número.')
                    continue
                
                new_task_name = input('Novo nome: ')
                task.update_task(task_list, new_task_name, task_id)
            
            case 4:
                task.show_tasks(task_list)
                try:
                    task_id = int(input('Número da tarefa que deseja completar: '))
                except:
                    print('Valor inválido. Tente inserir um número.')
                    continue
                task.complete_task(task_list, task_id)
                
            case 5:
                task.remove_completed_tasks(task_list)
                
            case 6:
                print("Saindo do Gerenciador de Tarefas...")
                return
            
            case _:
                print("Opção inválida. Tente novamente.")
                
    
if __name__ == "__main__":
    main()