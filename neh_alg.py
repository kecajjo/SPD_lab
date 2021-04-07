import time
import cmax

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

    print( dict(sorted(dict_of_priority.items(),key= lambda item: item[1], reverse=True)))
    return dict(sorted(dict_of_priority.items(),key= lambda item: item[1], reverse=True))

def neh(sorted_dict,table):
    #list_of =  [0] * len(sorted_dict)
    list_of=[]
    key_list = list(sorted_dict.keys())
    #print(key_list)
    list_of.append(key_list[0])
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
    tasks_order, cmax = neh(sorted_dict, table_from_file)
    duration = time.process_time() - start

    return  tasks_order,cmax,duration












