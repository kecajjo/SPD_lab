import cmax
import johnson_alg
import read
import math

class tabu_search:
    def __init__(self, task_lst):
        self.matrix = task_lst
        self.best_perm = []
        self.tabu_list = []
        self.neighbourhood_list = []
        self.best_cmax = math.inf
        self.neighbourhood_best_perm = []
        
    def execute(self, neighbourhood = "swap", strt_perm = "ascending"):
        self.best_perm = self.starting_perm(strt_type=strt_perm)
        self.neighbourhood_best_perm = self.best_perm
        self.best_cmax = cmax.calculate(self.perm, self.matrix)
        neighbourhood_cmax = self.best_cmax

        do_loop = True
        # if stop=="time":
        #   stop_param = time.now()
        # elif stop == "iterate":
        #   stop_param = 0
        while do_loop:
            neighbourhood_cmax = math.inf
            self.find_neighbourhood(type = neighbourhood)
            for neigh_num in range(self.neighbourhood_list):
                curr_cmax = cmax.calculate(self.neighbourhood_list[neigh_num], self.matrix)
                if curr_cmax < neighbourhood_cmax:
                    curr_cmax = neighbourhood_cmax
                    self.neighbourhood_best_perm = self.neighbourhood_list[neigh_num].copy()
            self.tabu_list.append(self.neighbourhood_best_perm)
            if neighbourhood_cmax < self.best_cmax:
                self.best_cmax = neighbourhood_cmax
                self.best_perm = self.neighbourhood_best_perm.copy()


        

    def find_neighbourhood(self, type="swap"):
        if type == "swap":
            self.find_neigh_swap()
        #elif:
            #TODO
        else:
            print("ERROR: find_neighbourhood option not known")

    def find_neigh_swap(self):
        self.neighbourhood_list.clear()
        #basic_perm = self.perm.copy()
        for i in range(len(self.perm)-1):
            current_perm = self.perm.copy()
            current_perm[i], current_perm[i+1] = self.perm[i+1], self.perm[i]
            self.neighbourhood_list.append(current_perm)
    
    def starting_perm(self, strt_type = "ascending"):
        perm = []
        if strt_type == "ascending":
            for i in range(len(self.matrix)):
                perm.append(i+1)
        else:
            print("ERROR: starting_perm option not known")
        return perm

if __name__ == "__main__":
    numberOfTask, numberOfMachine, matrix = read.read_from_file("dane.txt")
    tabu = tabu_search(matrix)
    tabu.find_neighbourhood()