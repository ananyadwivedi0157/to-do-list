import datetime
today = datetime.date.today()
print ('WELCOME!'.center(30))
print ('TO DO LIST'.center(30))
print ('1.Add a task')
print ('2.View task')
print ('3.Remove a task')
print ('4.Exit')
tasks=[]
option=0
task=""
while option!=4:
    option=int(input('Choose an option: ' ))
    if option==1:
        while task!="done":
         task=input('Add your task(type done to finish): ').lower()       
         if task!="done":
             date=input("add due date:")   
             tasks.append([task,date])
             print ("Task added!")
    elif option==2:
        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i][0]}")
            print(f"Due date: {tasks[i][1]}")
            due_date = datetime.datetime.strptime(tasks[i][1], "%d-%m-%Y").date()
            if today>due_date:
                print("task overdue")
            elif today==due_date:
                print("task due today")
    elif option==3:
        delete=int(input('which task would you like to remove? '))
        tasks.pop(delete-1)
    elif option==4:
        print('bye!')
    else:
        print('invalid command')
    

    