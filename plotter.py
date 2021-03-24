import matplotlib.pyplot as plt
import numpy as np

##############################################
# WszystkieZadania[x] zawiera zadania po kolei
# WszystkieZadania[][x] zawiera operacje(maszyny) po kolei
# WszystkieZadania[][][0 lub 1] na pozycji 0 jest
# czas startu, na pozycji 1 jest czas trwania
# Przykład
# WszystkieZadania = [
#    [[0.5, 1], [2, 1], [4, 6]],
#    [[0, 1], [1, 0.5], [4, 2]]
# ]
#############################################


def plot_gannt(task_list_3d, cmax):

    fig, ax = plt.subplots()

    iterator = 0  # Iterator pomocniczy
    num_of_tasks = len(task_list_3d)  # Liczba zadan
    num_of_operations = len(task_list_3d[0])  # Liczba operacji

    # Generowanie listy z współrzędnymi Y dla każdego zadania
    task_y_position = [[0.0]*2 for _ in range(num_of_tasks)]

    for i in range(num_of_tasks):
        task_y_position[i][0] = (i + 1) - 0.5 / 2
        task_y_position[i][1] = 0.5

    # Generowanie listy z nazwami dla maszyn
    machine_name = []
    for task in range(num_of_tasks + 1):
        machine_name.append("Maszyna " + str(task))

    # Zakres X
    xpos = np.arange(cmax * num_of_tasks)
    plt.xticks(xpos)

    # Zakres Y
    ypos = np.arange(num_of_tasks + 1)
    plt.yticks(ypos, machine_name[0:num_of_tasks + 1])

    # Ustawienie siatki
    plt.grid(axis="x", alpha=0.5)

    # Generowanie operacji
    for y_value in task_y_position:
        ax.broken_barh(task_list_3d[iterator], y_value, facecolor="lime", edgecolor="0")
        iterator += 1

    # Generowanie podpisow operacji
    for task in range(num_of_tasks):
        for operacja in range(num_of_operations):
            label = "O" + str(operacja + 1)
            ax.text(task_list_3d[task][operacja][0] + 0.1, task + 1, label)

    # Wyswietlenie diagramu :)
    plt.title("Diagram Gannta", fontsize=16)
    plt.show()


def convert_time_of_end_to_duration(table_to_change_end_time_to_duration, sorted_table_with_tasks_and_machines):
    table_from_function = table_to_change_end_time_to_duration
    for currMachine in range(len(table_from_function)):
        for currTask in range(len(table_from_function[currMachine])):
            table_from_function[currMachine][currTask][1]=sorted_table_with_tasks_and_machines[currTask][currMachine]
    return table_from_function




# w plotterze, trzeba podawać permutacje w argumentach,
# i to jakoś wykorzystać bo w tej chwili zawsze zadania są numerowane od 1
# w brute force mialem problem ze jesli macierz  ilosc zadan jest mniejsza od ilosci maszyn to wywala blad

#########################################
# wyj[][][0,1] 0 is start time 1 is end time
# wyj[][x][] x is task number
# wyj[y][][] y is machine number
# table[][z] z is machine number
# table[k][] k is task number
############################################
def prepare_data_to_plot(table):
    wyj = []
    for currMachine in range(len(table[0])):
        taskOfMachine = [[0,0]] * len(table)
        for currTask in range(len(table)):
            if currTask == 0:
                if currMachine == 0:
                    taskOfMachine[currTask] = [0, table[currTask][currMachine]]
                else:
                    #table[][] is duration, wyj[][][] is end time of task on previous machine
                    taskOfMachine[currTask] = [wyj[currMachine-1][currTask][1], wyj[currMachine-1][currTask][1]+table[currTask][currMachine]]
            else:
                if currMachine == 0:
                    #we take previous task's end time, #table[][] is duration of current task so after adding it gives us end time of current task
                    taskOfMachine[currTask] = [taskOfMachine[currTask-1][1], taskOfMachine[currTask-1][1]+table[currTask][currMachine]]
                else:
                    #max of {[previous machine, current task, end time], [current machine, previous task end time]} and is our starting point
                    startTimeOfTask = max(wyj[currMachine-1][currTask][1], taskOfMachine[currTask-1][1])
                    taskOfMachine[currTask] = [startTimeOfTask, startTimeOfTask+table[currTask][currMachine]]
        wyj.append(taskOfMachine)
    return wyj


def makePlot(tasksScheduled,cMax):
    table = prepare_data_to_plot(tasksScheduled)
    toShow = convert_time_of_end_to_duration(table, tasksScheduled)

    plot_gannt(toShow, cMax)
