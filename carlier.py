import  schrage
import  math
U_b = math.inf
best_perm = []
# n liczba zadan
# U wartosc funkcji celu -  Cmax
# UB gorne oszacowanie wartosci funkcji celu
# wartosc funkcji dla najlepszego obecnie rozwiazania

class carlier:
    def __init__(self):


    def execute_carlier(self, matrix_rpq):
        global U_b  # zmienna globalna
        global best_perm
        sch = schrage(matrix_rpq)
        U,perm = sch.schrange_alg(matrix_rpq)
        if U < U_b:
            U_b = U
            best_perm = perm

    def calculate_b(self, U, perm, matrix_rpq):
        p = 0
        for val in perm:
            r = matrix_rpq[val].prep_time
            p = max(p,r) + matrix_rpq[val].make_time
            if U == p + matrix_rpq[val].deliv_time:
                index = val
        return index

    def calculate_a(self,U, perm,matrix_rpq,b):
        q = matrix_rpq[b].deliv_time;
        task_b = perm.index(b)

        for val in perm:
            p = 0
            r = matrix_rpq[val].prep_time
            current_task_index = matrix_rpq[val].prep_time

            for i in range(current_task_index, task_b+1):
                p += matrix_rpq[perm[i]].make_time
            if U == r+p+q:
                return val #pierwsze zadanie takie podczas ktorego nie wystepuja przerwy

    def calculate_c(self, perm, matrix_rpq,a,b):
        a_task = perm.index(a)
        b_task = perm.index(b)

        for val in range(b_task,a_task-1,-1):
            if matrix_rpq[perm[val]].deliv_time < matrix_rpq[perm[b]].deliv_time:
                index = perm[val]
                return  index

        return [] # zbior pusty








