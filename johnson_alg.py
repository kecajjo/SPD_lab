def multiMachToTwoMach(numberOfTask, numberOfMachine, matrix):    
    #changing multi machine problem into 2 machine problem
    tasks = []
    for i in range(numberOfTask):
        machineTime = []
        summed = 0
        #summing first half of tasks
        if(numberOfMachine%2):
            for j in range(int(numberOfMachine/2)+1):
                summed += matrix[i][j]
        else:
            for j in range(int(numberOfMachine/2)):
                summed += matrix[i][j]
        machineTime.append((summed))
        #summing second half of tasks
        summed = 0
        for j in range(int(numberOfMachine/2), numberOfMachine):
            summed += matrix[i][j]
        machineTime.append((summed))
        tasks.append(machineTime)
    #print(tasks)
    
    return tasks

def johnson_alg(numberOfTask, numberOfMachine, matrix):
    tasks = multiMachToTwoMach(numberOfTask,numberOfMachine,matrix)
    print("\n\n\n")
    print(tasks)

    tasksSheduled = []
    tasksOrder = []
    fromBeg = 0
    fromEnd = 0

    #tasks[i][2] will be task number (counting from 0)
    for i in range(numberOfTask):
        tasks[i].append(i)

    for i in range(numberOfTask):
        minTime = float('inf')
        machineNum = 3#machine number that doesnt exist for easier debugging
        size = len(tasks)
        taskNum = 2147483647#the smallest max int

        # finding the shortest
        for j in range(size):
            if(tasks[j][0] < minTime):
                minTime = tasks[j][0]
                machineNum = 0
                taskNum = j
            if(tasks[j][1] < minTime):
                minTime = tasks[j][1]
                machineNum = 1
                taskNum = j

        #adding shortest task to sheduled list
        if(machineNum == 0):
            tasksSheduled.insert(fromBeg, matrix[tasks[taskNum][2]])
            tasksOrder.insert(fromBeg, tasks[taskNum][2]+1)
            fromBeg +=1
            del tasks[taskNum]
        elif(machineNum == 1):
            tasksSheduled.insert(len(tasksSheduled)-fromEnd, matrix[tasks[taskNum][2]])
            tasksOrder.insert(len(tasksOrder)-fromEnd, tasks[taskNum][2]+1)
            fromEnd +=1
            del tasks[taskNum]
        else:
            print("Error in func: johnson_alg")
    print("\n")
    print(tasksOrder)

