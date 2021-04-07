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

    return dict(sorted(dict_of_priority.items(),key= lambda item: item[1]))


def neh(sorted_dict,table):
    #list_of =  [0] * len(sorted_dict)
    list_of=[]
    list_of.append(sorted_dict)
    keys = sorted_dict.keys
    perm = [1]
    for index in range(1 , len(sorted_dict)):
        for index_of_perm in range(index+1):
            current_perm = perm
            current_perm.insert(index_of_perm,index)
            current_cmax = cmax.calculate(current_perm, table)
            print(current_cmax)











