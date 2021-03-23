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
    task_y_position = [[0.0]*num_of_tasks for _ in range(2)]

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


