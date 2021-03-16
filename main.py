import read
import johnson_alg as alg

x,y,z = read.read_from_file("dane.txt")
print(x)
print(y)
print(z)
alg.johnson_alg(x,y,z)