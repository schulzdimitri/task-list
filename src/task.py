class Task:    
    @staticmethod
    def add_task(task_name: str, task_list: list):
        task_list.append({"task_name": task_name, "completed": False, "id": len(task_list)})
        
        print(f"Tarefa '{task_name}' adicionada com sucesso!")

        
    @staticmethod
    def show_tasks(task_list: list):
        for index, task in enumerate(task_list, start=1):
            status = "✅" if task['completed'] else "⏹️ "
            print(f"{status} {index} - {task['task_name']}")

        
    @staticmethod
    def update_task(task_list: list, new_name: str, task_id: int):
        index = task_id - 1
        last_name = task_list[index]['task_name']
        
        task_list[index]['task_name'] = new_name
        print(f"Tarefa Renomeada de '{last_name}' para '{new_name}'")


    @staticmethod
    def complete_task(task_list: list, task_id: int):
        index = task_id - 1
        task_list[index]['completed'] = True
        
        print('Tarefa completada com sucesso!')
        Task.show_tasks(task_list)


    @staticmethod
    def remove_completed_tasks(task_list: list):
        for task in task_list:
            if task['completed']:
                task_list.remove(task)
        print('Tarefas concluidas removidas com sucesso!')
            
task = Task()