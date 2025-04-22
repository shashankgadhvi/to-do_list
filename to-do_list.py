# create a to-do list which includes
# adding , deleting , viewing or marking a task done.

def tasks():
    tasks = []
    while True:
        print()
        print('Select appropriate number for desired operation:')
        print('1.Add a task.')
        print('2.Delete a task')
        print('3 View all tasks.')
        print('4.Exit.')

        choice = int(input('Enter your choice: '))

        if choice==1:
            task_input = input('Enter the desired task: ')
            tasks.append(task_input)


        elif choice==2:
            if len(tasks)==0:
                print('No tasks to delete.')
            else:
                try:
                    delete_index = int(input('Enter the index of task you want to delete: '))
                    if 1<=delete_index<=len(tasks):
                        removed = tasks.pop(delete_index-1)
                        print()
                        print(f'Deleted {delete_index}th task from your list.')
                        print()
                    else:
                        print('Invalid task number.')    
                except ValueError:
                    print('Please enter a valid number.')


        elif choice==3:
            print()
            print('Here is your task display: ')
            for index, task in enumerate(tasks,start=1):
                print(f'{index}. {task}')
                print('------------------')
            print()


        elif choice==4:
            print('Exiting..')
            return
tasks()