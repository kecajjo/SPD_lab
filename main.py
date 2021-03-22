import read
import johnson_alg as alg
import cmax as cmax
import brute_force as brute
import time
import plotter
x,y,z = read.read_from_file("dane.txt")
#print(x)
#print(y)
alg.johnson_alg(x,y,z)


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
def prepare_data_to_plot(permutation, table):
    wyj = [[0,0]] * len(permutation)
    print(wyj)
    print(permutation)
    z = 0
    for i in permutation:
        j = i - 1
        if z == 0:
            wyj[z] = [0, table[j][0]]
        elif z == 1:
            wyj[z] = [wyj[j-1][1], table[j][0]]
        else:
            wyj[z] = [wyj[j-1][0] + wyj[j-1][1], table[j][0]]
        z+=1
    return wyj

#cos=prepare_data_to_plot(perm,z)
#print(cos)




