import cmax as cmax
import itertools
import time

# this function provides a brute force method
# input : table
# table[][]
# example index
# table[current_number_of_machine][current_number_of_task]
# output
# best_current_perm - best current order of tasks
# smallest_present_value_cmax - best cmax
# duration - time of executing function
#
def brute_force(table):
        start_time = time.process_time()
        numbers_of_tasks = []
        for i in range(len(table)):
            numbers_of_tasks.append(i+1)                        # because we count tasks from 1
        permutations = itertools.permutations(numbers_of_tasks) #all possible combinations
        i=0
        smallest_present_value_cmax=0                           #smallest current value of cmax
        best_current_perm = []                                  #best current order of tasks
        current_value = 0
        for perm in permutations:
            current_value = cmax.calculate(perm, table)         #another cmax
            if i == 0:
                smallest_present_value_cmax = current_value     #first iteration
                best_current_perm = perm
            i += 1
            if current_value < smallest_present_value_cmax:       #if the new one is smaller than the smallest so far
                smallest_present_value_cmax = current_value
                best_current_perm = perm
        duration = time.process_time() - start_time
        return best_current_perm, smallest_present_value_cmax, duration


#This function sort our table by order from perm
#this feature allow us to easier plotting
#function return sorted_table depends on perm
def sort_table_by_perm(tableToSort, perm):
    sorted_table = []
    for task in perm:
        sorted_table.append(tableToSort[task-1])
    return sorted_table

#This function do executing of brute force with sorting table and return the most important things
def execute_brute_force(table):
    best_current_perm, smallest_present_value, duration = brute_force(table)
    sorted_table = sort_table_by_perm(table,best_current_perm)

    return best_current_perm, sorted_table, smallest_present_value, duration
