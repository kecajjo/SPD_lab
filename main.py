import read
import johnson_alg as alg

x,y,z = read.read_from_file("dane.txt")
print(x)
print(y)
alg.johnson_alg(x,y,z)


def calculate_cmax(permutation, number_of_machines, table):
    m = [0] * len(permutation)
    for i in permutation:
        for j in range(0, number_of_machines):
            if j == 0:
                m[j] += table[i-1][j] #i-1 bo w wektorze permutacji mamy liczby od 1 i bysmy wyleciali poza tablice
            else:
                m[j] = max(m[j], m[j-1]) + table[i-1][j]
    return max(m)



perm = [3, 17, 9, 8, 15, 14, 11, 16, 13, 19, 6, 4, 5, 18, 1, 2, 10, 7, 20, 12]
result = calculate_cmax(perm,y, z)
print(result)
