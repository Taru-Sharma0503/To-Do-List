import csv
rows=[]
l=[]
count=0
with open('todoList.csv','w',newline='') as f:
    write=csv.writer(f)
    write.writerow(['Task','Status'])
choice=input(("Do you want to add a task? (yes/no): "))
if(choice.lower()=='yes'):
    count=1
    i=int(input("Enter the number of tasks you want to add: "))
    for j in range(i):
        task=input("Enter the task you want to add: ")
        with open('todoList.csv','a',newline='') as f:
            write=csv.writer(f)
            write.writerow([task,'Not Done'])
else:
    print("No task added.")
if(count==0):
    print("Your To-Do List is empty.")
else:
    print("Your current To-Do List is:")
    with open('todoList.csv','r',newline='') as f:
        read=csv.reader(f)
        for row in read:
            print(row[0],'-',row[1])
    with open('todoList.csv','r',newline='') as f:
        read=csv.reader(f)
        for row in read:
            l.append(row)
choice=input("Do you want to mark any task as done? (yes/no): ")
if(count==0):
    print("No tasks to mark as done.")
else:
    if(choice.lower()=='yes'):
        i=int(input("Enter the number of tasks you want to mark as done: "))
        for j in range(i):
            task=input("Enter the task you want to mark as done: ")
            with open('todoList.csv','r',newline='') as f:
                read=csv.reader(f)
                for row in read:
                    if(row[0]==task):
                        l[l.index(row)][1]='Done'
    with open ('todoList.csv','w',newline='') as f:
        write=csv.writer(f)
        write.writerows(l)
choice=input("Do you want to delete any task? (yes/no): ")
if(count==0):
    print("No tasks to delete.")
else:
    if(choice.lower()=='yes'):
        i=int(input('Enter the number of tasks you want to delete: '))
        for j in range(i):
            task=input('Enter the task you want to delete: ')
            with open('todoList.csv','r',newline='') as f:
                read=csv.reader(f)
                for row in read:
                    if(row[0]!=task and row[0]!='Task'):
                        rows.append(row)
    else:
        with open('todoList.csv','r',newline='') as f:
            read=csv.reader(f)
            for row in read:
                rows.append(row)
        with open('todoList.csv','w',newline='') as f:
            write=csv.writer(f)
            write.writerow(['Task','Status'])
            write.writerows(rows)
    print("Final To-Do List:")
    for row in rows:
        print(row[0],'-',row[1])