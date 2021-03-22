import read
import johnson_alg as alg
import cmax as cmax
import brute_force as brute
import time
import plotter
x,y,z = read.read_from_file("dane.txt")
print(x)
print(y)
#alg.johnson_alg(x,y,z)


perm, cmax,time  = brute.brute_force(z)
print(cmax)
print(perm)
print(time)
#perm = [3, 17, 9, 8, 15, 14, 11, 16, 13, 19, 6, 4, 5, 18, 1, 2, 10, 7, 20, 12]


plotter.plot_gannt([
    [[0.5, 1], [2, 1], [4, 6]],
    [[0, 1], [1, 0.5], [4, 2]]
 ],50)

#result = cmax.calculate(perm, z)
#print(result)

def prepare_data_to_plot(permutation, table):
    for x in permutation: x-=1       #zeby byly teraz od 0



