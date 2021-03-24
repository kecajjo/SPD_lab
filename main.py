import read
import johnson_alg as alg
import cmax as cmax
import brute_force as brute
import time
import plotter


numberOfTask, numberOfMachine, matrix = read.read_from_file("dane.txt")

tasksOrderBrute, tasksScheduledBrute, cMaxBrute, durationBrute = brute.brute_force(matrix)
tasksOrderJohn, tasksScheduledJohn, cMaxJohn, durationJohn = alg.johnson_alg(numberOfTask, numberOfMachine, matrix)
print("Tasks order from brute force: {:}\nTasks order for Johnson algorithm: {:}" .format(tasksOrderBrute, tasksOrderJohn))
print("Cmax brute force: {:}\nCmax for Johnson algorithm: {:}".format(cMaxBrute,cMaxJohn))
print("Time to find solution for brute force: {:}\nTime to find solution for Johnson algorithm: {:}".format(durationBrute,durationJohn))

plotter.makePlot(tasksScheduledJohn,cMaxJohn)

#perm, cmax,time  = brute.brute_force(tableFromFile)
#perm = [3, 17, 9, 8, 15, 14, 11, 16, 13, 19, 6, 4, 5, 18, 1, 2, 10, 7, 20, 12]

plotter.makePlot(sorted_table,smallest_present_value)






