import read
import johnson_alg as alg
import cmax as cmax
import brute_force as brute
import time
import plotter
x,y,z = read.read_from_file("dane.txt")
#print(x)
#print(y)
cos, wazne, coscos, coscoscos = alg.johnson_alg(x,y,z)


#perm, cmax,time  = brute.brute_force(z)
#print(cmax)
#print(perm)
#print(time)
#perm = [3, 17, 9, 8, 15, 14, 11, 16, 13, 19, 6, 4, 5, 18, 1, 2, 10, 7, 20, 12]


plotter.plot_gannt([
    [[0, 4], [4, 4], [8, 10], [18, 6], [24, 2]],
    [[4, 5], [9, 1], [18, 4], [24, 10], [34, 3]]
 ], 47)

#result = cmax.calculate(perm, z)
#print(result)


# w johnsonie trzeba dodac liczenie czasu
# w plotterze, trzeba podawać permutacje w argumentach,
# i to jakoś wykorzystać bo w tej chwili zawsze zadania są numerowane od 1
# w brute force mialem problem ze jesli macierz  ilosc zadan jest mniejsza od ilosci maszyn to wywala blad
#tu jest funkcja ktora przygotowuje dane, ale nie dokońca działa

#########################################
# wyj[][][0,1] 0 is start time 1 is end time
# wyj[][x][] x is task number
# wyj[y][][] y is machine number
# table[][z] z is machine number
# table[k][] k is task number
############################################
def prepare_data_to_plot(table):
    #wyj = [[0,0]] * len(permutation)
    wyj = []
    #print(wyj)
    #print(permutation)
    for currMachine in range(len(table[0])):
        taskOfMachine = [[0,0]] * len(table)
        for currTask in range(len(table)):
            if currTask == 0:
                if currMachine == 0:
                    taskOfMachine[currTask] = [0, table[currTask][currMachine]]
                else:
                    #table[][] is duration, wyj[][][] is end time of task on previous machine
                    taskOfMachine[currTask] = [wyj[currMachine-1][currTask][1], wyj[currMachine-1][currTask][1]+table[currTask][currMachine]]
            else:
                if currMachine == 0:
                    #we take previous task's end time, #table[][] is duration of current task so after adding it gives us end time of current task
                    taskOfMachine[currTask] = [taskOfMachine[currTask-1][1], taskOfMachine[currTask-1][1]+table[currTask][currMachine]]
                else:
                    #max of {[previous machine, current task, end time], [current machine, previous task end time]} and is our starting point
                    startTimeOfTask = max(wyj[currMachine-1][currTask][1], taskOfMachine[currTask-1][1])
                    taskOfMachine[currTask] = [startTimeOfTask, startTimeOfTask+table[currTask][currMachine]]
        wyj.append(taskOfMachine)
    return wyj

perm, cmax,time  = brute.brute_force(z)
print(wazne)
print("\n\n\n\n")
cos=prepare_data_to_plot(wazne)
plotter.plot_gannt(cos,50)
print("\n\n\n\n")
print(cos)




