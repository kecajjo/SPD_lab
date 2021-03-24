import cmax as cmax
import itertools
import time
def brute_force(table):
        start_time = time.process_time()
        numbers_of_tasks = []
        for i in range(len(table)):
            numbers_of_tasks.append(i+1) # bo liczymy zadania od 1
        permutations = itertools.permutations(numbers_of_tasks) #wszystkie mozliwe kombinacji
        i=0
        smallest_present_value=0#najmniejsza obecna wartosc cmax
        best_current_perm = []          #najlepsza obecna kolejnosc zadan
        current_value = 0
        for perm in permutations:
            current_value = cmax.calculate(perm, table)
            if i == 0:
                smallest_present_value = current_value #pierwsza iteracja
                best_current_perm = perm
            i += 1
            if current_value < smallest_present_value:       #jesli nowa jest mniejsza od tej najmniejszej dotychczas
                smallest_present_value = current_value
                best_current_perm = perm
        duration = time.process_time() - start_time
        return best_current_perm, smallest_present_value, duration

def sort_table_by_perm(tableToSort, perm):
    sorted_table = []
    for task in perm:
        sorted_table.append(tableToSort[task-1])
    return sorted_table

def execute_brute_force(table):
    best_current_perm, smallest_present_value, duration = brute_force(table)
    sorted_table = sort_table_by_perm(table,best_current_perm)

    return best_current_perm, sorted_table, smallest_present_value, duration