import  schrage
import  math
UB = math.inf
best_perm = []
# n liczba zadan
# U wartosc funkcji celu -  Cmax
# UB gorne oszacowanie wartosci funkcji celu
# wartosc funkcji dla najlepszego obecnie rozwiazania

class carlier:
    def __init__(self):
        pass

    def execute_carlier(self, matrix_rpq):
        global UB  # zmienna globalna
        global best_perm
        sch = schrage.schrage()
        U,perm = sch.schrange_alg(matrix_rpq)
        if U < UB:
            UB = U
            best_perm = perm
        b = self.calculate_b(U,perm,matrix_rpq)
        a = self.calculate_a(U,perm,matrix_rpq,b)
        c = self.calculate_c(perm,matrix_rpq,a,b)

        if c == -1:
            return

       # K = []
        #for i in range(c+1,b+1):
         #   K.append(i)
        rK = []
        qK = []
        pK = 0

        for val in perm[perm.index(c)+1:perm.index(b)+1]:
            rK.append(matrix_rpq[val].prep_time)
            qK.append(matrix_rpq[val].deliv_time)
            pK += matrix_rpq[val].make_time

        qK_min = min(qK)
        rK_min = min(rK)
        pK_min = pK
        rpq_sum = qK_min + rK_min + pK_min

        temp = matrix_rpq[c].prep_time
        matrix_rpq[c].prep_time = max(matrix_rpq[c].prep_time,rK_min+pK_min)

        pKc_min = pK_min + matrix_rpq[c].make_time
        qKc_min = min(qK_min,matrix_rpq[c].deliv_time)
        rKc_min = min(rK_min,matrix_rpq[c].prep_time)
        rpq_c_sum = pKc_min + qKc_min + rKc_min

        sch_i = schrage.schrage()
        LB = sch_i.schrange_alg_interrupt(matrix_rpq)


        LB = max(rpq_sum,rpq_c_sum,LB )
        UB_cos = UB
        if LB < UB :
            self.execute_carlier(matrix_rpq)
        matrix_rpq[perm[c]].prep_time = temp



        #start_time_c = max(matrix_rpq[perm[c]].prep_time, rK_min + pK_min)
        temp = matrix_rpq[perm[c]].deliv_time
        matrix_rpq[perm[c]].deliv_time = max(matrix_rpq[perm[c]].deliv_time, qK_min + pK_min)

        pKc_min = pK_min + matrix_rpq[perm[c]].make_time
        qKc_min = min(qK_min, matrix_rpq[perm[c]].deliv_time)
        rKc_min = min(rK_min, matrix_rpq[perm[c]].prep_time)
        rpq_c_sum = pKc_min + qKc_min + rKc_min

        LB = sch.schrange_alg_interrupt(matrix_rpq)

        LB = max(rpq_sum, rpq_c_sum, LB)

        if LB < UB:
            self.execute_carlier(matrix_rpq)
        matrix_rpq[perm[c]].deliv_time = temp










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
            current_task_index = perm.index(val)

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

        return -1 # zbior pusty




if __name__ == "__main__":
    car = carlier()
    matrix = schrage.read_from_file("dane.txt")
    car.execute_carlier(matrix)
    print(best_perm)
    print(UB)








