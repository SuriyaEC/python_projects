
print("************wellcome****************".center(90))
print("    *** Manage Your Tasks Here***   ".center(90))

userinput1=input("enter 1->add new task  2->view task list  3->change task status: ")

tasks=[]

if userinput1== '1':
    t=input("enter title: ")
    d=input("describe you task: ")
    date=input("enter the end date: ")
    def addTask(title,description,due_date,status):
        Ntask=[]
        Ntask.append(title)
        Ntask.append(description)
        Ntask.append(due_date)
        Ntask.append(status)
        tasks.append(Ntask)
       
    addTask(t,d,date,status="not completed")
    print("successfully added")

elif userinput1 == '2':
    def viewTask():
        return tasks

    print(viewTask())

elif userinput1 == '3':
    def changestatus(title,nstatus):
        for task in tasks:
            if task[0]== title:
                task[3] = nstatus
    changestatus(input("enter title: "),input("enter status:"))
    print("changed successfully")

else :
    print("invalid entry")
