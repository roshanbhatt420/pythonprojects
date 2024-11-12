print("TODO list sytem")
print("This is just command line version of todo list")
print("lets Add some task")
tasks=[{"task":"By Groceris","completed":False}]
while(1):
    print("enter 0 for exit from program")
    print("1 for add new tasks\n 2 for View tasks \n 3 for mark task as completed\n 4 for delete task \n 5 for Edit task\n6 for save task in file")
    user_choice=(input(" Your Number is  "))
    if user_choice==0:
        print("you closed the program")
        exit()
    else:
        match user_choice:
            case 1:
                new_tasks=str(input('Enter your New task'))
                tasks.append(new_tasks)
                print(tasks)
