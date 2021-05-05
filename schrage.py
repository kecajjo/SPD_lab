
import operator

class data:
    def __init__(self,prepare, make, delivery):
        self.prep_time = prepare
        self.make_time = make
        self.deliv_time = delivery

class schrage:
    def __init__(self):
        self.tasks_number=0
        self.stages_number=3
        self.matrix_tasks=[]
        self.part_perm = []
        self.max_end_time = 0


    def schrange_alg(self):
        N_g = []
        N_n = self.matrix_tasks.copy()
        #current_time = min(N_n)[0] #najmniejszy czas przygotowania w zadaniach
        current_time =  min(N_n,key= lambda data:data.prep_time).prep_time

        while(len(N_g) != 0 or len(N_n) != 0):
            while(len(N_n) != 0 and min(N_n,key= lambda data:data.prep_time).prep_time <= current_time):
                #z nastepna linijka cos jest nie tak
                j = N_n.index(min(N_n, key= lambda data:data.prep_time))
                N_g.append(N_n.pop(j))
            if len(N_g) == 0:
                current_time = min(N_n, key= lambda data:data.prep_time).prep_time
            else:
                j = N_g.index(max(N_g, key= lambda data:data.deliv_time))
                tmp = N_g.pop(j)
                self.part_perm.append(j+1)
                current_time += tmp.make_time
                self.max_end_time = max(self.max_end_time, current_time + tmp.deliv_time)

        return self.max_end_time, self.part_perm

                




    def read_from_file(self,file_name):
        f = open(file_name, "r")

        line_from_file = f.readline()

        list_from_file = line_from_file.split()
        number_of_task = int(list_from_file[0])
        number_of_machine = int(list_from_file[1])

        loaded_table_from_file = []


        for i in range(number_of_task):
            line_from_file = f.readline()
            list_from_file = line_from_file.split()

            prep_time = int(list_from_file[0])
            make_time = int(list_from_file[1])
            deliv_time = int(list_from_file[2])
            rpq = data(prep_time,make_time,deliv_time)
            self.matrix_tasks.append(rpq)








if __name__ == "__main__":
    sch = schrage()
    sch.read_from_file("dane.txt")
    #sch.matrix_tasks[0].prep_time
    x,y = sch.schrange_alg()
    print(x)
    #print(matrix[2].index(max(matrix,key=operator.itemgetter(2))[2]))
