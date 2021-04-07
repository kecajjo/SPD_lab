import read
import johnson_alg as alg
import cmax as cmax
import time
import plotter
import neh_alg


numberOfTask, numberOfMachine, matrix = read.read_from_file("dane.txt")
perm = [1,3]
print(cmax.calculate(perm,matrix))
x = neh_alg.calculate_priority_from_table(matrix)
neh_alg.neh(x,matrix)
#neh_alg.calculate_priority_from_table(matrix)

#tasksOrderBrute, tasksScheduledBrute, cMaxBrute, durationBrute = brute.execute_brute_force(matrix)
tasksOrderJohn, tasksScheduledJohn, cMaxJohn, durationJohn = alg.johnson_alg(numberOfTask, numberOfMachine, matrix)
#print(cMaxJohn)









#print("Tasks order from brute force: {:}\nTasks order for Johnson algorithm: {:}" .format(tasksOrderBrute, tasksOrderJohn))
#print("Cmax brute force: {:}\nCmax for Johnson algorithm: {:}".format(cMaxBrute,cMaxJohn))
#print("Time to find solution for brute force: {:}\nTime to find solution for Johnson algorithm: {:}".format(durationBrute,durationJohn))

#plotter.makePlot(tasksScheduledJohn,cMaxJohn,tasksOrderJohn)

#perm, cmax,time  = brute.brute_force(tableFromFile)
#perm = [3, 17, 9, 8, 15, 14, 11, 16, 13, 19, 6, 4, 5, 18, 1, 2, 10, 7, 20, 12]







