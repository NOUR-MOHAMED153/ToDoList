
def add_task(): 
    #get task from user 
    task = input("\nenter a task : ")
    #task info ( complete or not )
    task_info = {"task":task, "completed" : False}
    #add task to the list 
    tasks.append(task_info)
    print("\ntask added to the list succefully. \n")
    #ask user if he want to add more task in the list
    again = str(input("Do you want to add any thing else ? ")).lower()
    if again == "yes" or again == "y":
        add_task()
def mark_task_as_complete(): 
    #get list of incomplete tasks
    incomplete_tasks = []
    for task in tasks:
        if task["completed"] == False:
            incomplete_tasks.append(task)
    #show them to the user
    for i,task in enumerate(incomplete_tasks):
        print(i+1,"-",task["task"])
    #get the task from user
    task_numper = int(input("\nwhat task do you want to mark ? "))
    #mark the task as complete
    incomplete_tasks[task_numper-1]["completed"] = True
    #print a message to the user
    print("\nthe task marked complete.")
def remove_task():
    #show the list to the user
    for i,task in enumerate(tasks):
        if task["completed"] == True:
            print(f"\n{i+1}-",task['task'],"  ( Completed )")
        else:
            print(f"\n{i+1}-",task["task"])
    #take the task from user
    task_num = int(input("\nWhat task do you want to remove ? "))
    #remove the task from the list
    task_num = task_num-1
    tasks.remove(tasks[task_num])
    print("\nthe task removed succefully. ")
def show_list(): 
    if tasks == []:
        print("\nNothing in the list yet ! ")
    for i in tasks:
        if i["completed"] == True:
            print("\n-",i['task'],"  ( Completed )")
        else:
            print("\n-",i["task"])
print("  Welcome again! \n------------------")
message = "\n1: Show the list \n2: Add tasks to the list \n3: Mark task as complete\n4: remove task from the list \n5: Quit\n\n--> "
tasks = []
while True:
    try:
        choice = int(input(message))
    except ValueError:
        choice = ''
    if choice == 1:
        show_list()
    elif choice == 2:
        add_task() 
    elif choice == 3:
        mark_task_as_complete()
    elif choice == 4:
        remove_task()
    elif choice == 5:
        break
    else:
        print("invalid choice, please try again\n ")