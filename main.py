import read
import johnson_alg as alg
import cmax as cmax
import brute_force as brute
import time
import plotter


x,y,z = read.read_from_file("dane.txt")

tasksOrder, tasksSheduled, duration, cMax = alg.johnson_alg(x,y,z)
best_current_perm, sorted_table, smallest_present_value, duration =brute.execute_brute_force(z)


#perm, cmax,time  = brute.brute_force(tableFromFile)
#perm = [3, 17, 9, 8, 15, 14, 11, 16, 13, 19, 6, 4, 5, 18, 1, 2, 10, 7, 20, 12]

plotter.makePlot(sorted_table,smallest_present_value)






