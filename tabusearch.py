import cmax
import johnson_alg
import read
import math
import time

class tabu_search:
    def __init__(self, task_lst):
        self.matrix = task_lst
        self.best_perm = []
        self.tabu_list = []
        self.neighbourhood_list = []
        self.best_cmax = math.inf
        self.neighbourhood_best_perm = []
    #funkcja wykonujaca tabusearch wraz z podanymi parametrami
    #neighbourhood - jaka opcja do szukania sasiedzctwa , swap czy insert
    #strt_perm - kolejnosc poczatkowa zadan do modyfikacji
    #stop - pod jakim wzgledem zatrzymamy funkcje - albo po czasie albo po iteracjach
    #stop_value - warunek stopu, gdy patrzymy na czas, jest to ilosc sekund, jesli patrzymy na iteracje - ilosc iteracji
    #tabu_length - dlugosc listy tabu, ma wplyw na rozwiazanie, im dluzsza tym lepiej
    def execute(self, neighbourhood = "swap", strt_perm = "ascending", stop = "iterate",stop_value = 1000, tabu_length = 100):
        self.best_perm = self.starting_perm(strt_type=strt_perm)
        self.neighbourhood_best_perm = self.best_perm
        self.best_cmax = cmax.calculate(self.neighbourhood_best_perm, self.matrix)
        neighbourhood_cmax = self.best_cmax

        do_loop = True

        if stop == "time":
            stop_param = time.process_time()
        elif stop == "iterate":
            stop_param = 0
        else:
            print("ERROR: execute option not known")
        while do_loop:
            neighbourhood_cmax = math.inf
            self.find_neighbourhood(type = neighbourhood)
            for neigh_num in range(len(self.neighbourhood_list)):
                curr_cmax = cmax.calculate(self.neighbourhood_list[neigh_num], self.matrix)
                if curr_cmax < neighbourhood_cmax:
                    neighbourhood_cmax = curr_cmax
                    self.neighbourhood_best_perm = self.neighbourhood_list[neigh_num].copy()
            if len(self.tabu_list) >= tabu_length:
                self.tabu_list.pop(0)
            self.tabu_list.append(self.neighbourhood_best_perm)
            if neighbourhood_cmax < self.best_cmax:
                self.best_cmax = neighbourhood_cmax
                self.best_perm = self.neighbourhood_best_perm.copy()
            if stop == "time":
                if time.process_time() - stop_param > stop_value:
                    do_loop = False
            if stop == "iterate":
                stop_param += 1
                if stop_param > stop_value:
                    do_loop = False




        
    #funkcja szukająca sąsiedztwo, w zależności od parametru type
    def find_neighbourhood(self, type="swap"):
        if type == "swap":
            self.find_neigh_swap()
        #elif:
            #TODO
        else:
            print("ERROR: find_neighbourhood option not known")

    #funkcja szukajaca sasiedzctwa poprzez swap, zamienia dwa sasiednie elementy
    def find_neigh_swap(self):
        self.neighbourhood_list.clear()
        #basic_perm = self.perm.copy()
        for i in range(len(self.neighbourhood_best_perm)-1):
            current_perm = self.neighbourhood_best_perm.copy()
            current_perm[i], current_perm[i+1] = self.neighbourhood_best_perm[i+1], self.neighbourhood_best_perm[i]
            on_tabu_list = False #zabezpieczenie przed wpisywaniem czegos do tabu list, jesli bylo juz przedtem
            for i in self.tabu_list:
                if i == current_perm:
                    on_tabu_list = True

            if on_tabu_list == False:
                self.neighbourhood_list.append(current_perm)

    #funkcja która zwraca permutacje w zależności od parametru, do wyboru, domyslna kolejnosc albo z algorytmu johnsona
    def starting_perm(self, strt_type = "ascending"):
        perm = []
        if strt_type == "ascending":
            for i in range(len(self.matrix)):
                perm.append(i+1)
        elif strt_type == "johnson":
            perm,x,y,z = johnson_alg.johnson_alg(len(matrix),len(matrix[0]),matrix)
        else:
            print("ERROR: starting_perm option not known")
        return perm

if __name__ == "__main__":
    numberOfTask, numberOfMachine, matrix = read.read_from_file("dane.txt")
    tabu = tabu_search(matrix)
    tabu.find_neighbourhood()
    tabu.execute(strt_perm="johnson")
    print(tabu.best_cmax)