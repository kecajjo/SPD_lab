import time
import cmax
import plotter

def calculate_priority_from_table(table_from_file):
    dict_of_priority ={}
    number_of_tasks = len(table_from_file)
    number_of_machines = len(table_from_file[0])
    task_order = [0] * number_of_tasks
    summary=[0] * number_of_tasks
    for index_of_task in range(number_of_tasks):
        for index_of_machine in range(number_of_machines):
            summary[index_of_task] += table_from_file[index_of_task][index_of_machine]
        dict_of_priority.update({index_of_task+1:summary[index_of_task]})

    #print( dict(sorted(dict_of_priority.items(),key= lambda item: item[1], reverse=True)))
    return dict(sorted(dict_of_priority.items(),key= lambda item: item[1], reverse=True))

def neh(sorted_dict,table):
    key_list = list(sorted_dict.keys())
    perm = []    
    perm.append(key_list[0])
    for index in range(1 , len(sorted_dict)):
        min_cmax = 1000000000#very big number
        index_of_min = 1000000#not existing index
        for index_of_perm in range(index+1):
            current_perm = perm.copy()
            current_perm.insert(index_of_perm, key_list[index])
            current_cmax = cmax.calculate(current_perm, table)
            if current_cmax < min_cmax:
                index_of_min = index_of_perm
                min_cmax = current_cmax
            #print(current_cmax)
        perm.insert(index_of_min, key_list[index])

    return perm, min_cmax
    #print("Permutacja od NEHa: {}".format(perm))
    #print("CMAX od NEHa: {}".format(min_cmax))

def execute_neh(table_from_file):
    sorted_dict = calculate_priority_from_table(table_from_file)
    start = time.process_time()
    #odpalamy modyfikacje
    tasks_order, cmax = neh_mod1(sorted_dict, table_from_file)
    duration = time.process_time() - start

    return  tasks_order,cmax,duration

def neh_mod1(sorted_dict,table):
    key_list = list(sorted_dict.keys())
    perm = []    
    perm.append(key_list[0])
    for index in range(1 , len(sorted_dict)):
        min_cmax = 1000000000#very big number
        index_of_min = 1000000#not existing index
        for index_of_perm in range(index+1):
            current_perm = perm.copy()
            current_perm.insert(index_of_perm, key_list[index])
            current_cmax = cmax.calculate(current_perm, table)
            if current_cmax < min_cmax:
                index_of_min = index_of_perm
                min_cmax = current_cmax
            #print(current_cmax)
        perm.insert(index_of_min, key_list[index])
        #sorting table for find_crit_path function
        sorted_table = sort_table_by_perm(table, perm)
        #print(sorted_table)
        crit_path = find_crit_path(sorted_table)
        longest_operation = 0
        perm_index_to_be_removed = 100000000#non existing index
        for index_in_crit_path in range(len(crit_path)):
            if(crit_path[index_in_crit_path][2] > longest_operation):
                longest_operation = crit_path[index_in_crit_path][2]
                perm_index_to_be_removed = crit_path[index_in_crit_path][0]
        task_num = perm.pop(perm_index_to_be_removed)
        min_cmax = 1000000000#very big number
        index_of_min = 1000000#not existing index
        for index_of_perm in range(index+1):
            current_perm = perm.copy()
            current_perm.insert(index_of_perm, task_num)
            current_cmax = cmax.calculate(current_perm, table)
            if current_cmax < min_cmax:
                index_of_min = index_of_perm
                min_cmax = current_cmax
            #print(current_cmax)
        perm.insert(index_of_min, task_num)


    print(perm)
    return perm, min_cmax    
###############################
# needs sorted table
# crit_path_reversed[nb_of_task, nb_of_mach, operation_time]
###############################
def find_crit_path(table):
    start_end_task_times = plotter.prepare_data_to_plot(table)
    nb_of_task = len(start_end_task_times[0])
    nb_of_mach = len(start_end_task_times)
    curr_task = len(start_end_task_times[0])-1
    curr_mach = len(start_end_task_times)-1
    crit_path = []
    for i in range(0, nb_of_mach+nb_of_task-2):
        if(curr_task > 0 and curr_mach > 0): 
            if(start_end_task_times[curr_mach][curr_task][0] == start_end_task_times[curr_mach-1][curr_task][1]):
                crit_path.insert(0, [curr_task, curr_mach, start_end_task_times[curr_mach][curr_task][1] - start_end_task_times[curr_mach][curr_task][0]])
                curr_mach = curr_mach-1
            else:
                crit_path.insert(0, [curr_task, curr_mach, start_end_task_times[curr_mach][curr_task][1] - start_end_task_times[curr_mach][curr_task][0]])
                curr_task = curr_task-1
        elif curr_task <=0:
            curr_task = 0
            crit_path.insert(0, [curr_task, curr_mach, start_end_task_times[curr_mach][curr_task][1] - start_end_task_times[curr_mach][curr_task][0]])
            curr_mach = curr_mach-1
        elif curr_mach <=0:
            curr_mach = 0
            crit_path.insert(0, [curr_task, curr_mach, start_end_task_times[curr_mach][curr_task][1] - start_end_task_times[curr_mach][curr_task][0]])
            curr_task = curr_task-1
        else:
            print("\n\nERROR IN FIND_CRIT_PATH FUNCTION\n\n")
    crit_path.insert(0, [0,0, start_end_task_times[0][0][1] - start_end_task_times[0][0][0]])
    #print("")
    #print(crit_path)
    return crit_path
###################################juz zrobione#
#
# aktualnie dostajemy sciezke krytyczna z posortowanej tablicy, wiec zeby odzyskac
# numer taska musimy przeszukac crit_path[x][2], znalezc najwiekszy element i zobaczyc dla jakiego x
# nastepnie sprawdzic jaki to byl oryginalny indeks, przez liste permutacji [x]
# usunac te zadanie w nehu i wstawiac je na wszystkie mozliwe miejsca sprawdzajac gdzie jest najmniejszy Cmax
####################################

#This function sort our table by order from perm
#this feature allow us to easier plotting
#function return sorted_table depends on perm
def sort_table_by_perm(tableToSort, perm):
    sorted_table = []
    for task in perm:
        sorted_table.append(tableToSort[task-1])
    return sorted_table










