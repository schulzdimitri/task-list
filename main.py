from src.task import task


def main():
    task_list = []
    
    print("\n Task Management Menu \n")
    print("1 - Add Task")
    print("2 - See all Tasks")
    print("3 - Update Task")
    print("4 - Complete Task")
    print("5 - Delete completed tasks")
    print("6 - Exit")
    
    while True:
        try:
            choice = int(input("Enter the desired option: "))
        except:
            print('Invalid value! Try entering a number.')
            continue
        
        match choice:
            case 1:
                task_name = input("Enter the task name:")
                task.add_task(task_name, task_list)
                
            case 2:
                task.show_tasks(task_list)
                
            case 3:
                task.show_tasks(task_list)
                try:
                    task_id = int(input('Enter the number of the task you wish to change: ')) 
                except:
                    print('Invalid value! Try entering a number.')
                    continue
                
                new_task_name = input('New task name: ')
                task.update_task(task_list, new_task_name, task_id)
            
            case 4:
                task.show_tasks(task_list)
                try:
                    task_id = int(input('Number of the task you wish to complete: '))
                except:
                    print('Invalid value! Try entering a number.')
                    continue
                task.complete_task(task_list, task_id)
                
            case 5:
                task.remove_completed_tasks(task_list)
                
            case 6:
                print("Exiting Task Manager...")
                return
            
            case _:
                print("Invalid option! Try again.")
                
    
if __name__ == "__main__":
    main()
