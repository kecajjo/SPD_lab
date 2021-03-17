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
    print(tasks)
