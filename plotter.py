import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

##############################################
# TasksPos[][x] zawiera zadania po kolei
# TasksPOs[][][0 lub 1] na pozycji 0 jest
# czas startu, na pozycji 1 jest czas trwania
##############################################
TasksPos = [
    [[0.5, 1], [2, 1], [4, 6]],
    [[0, 1], [1, 0.5], [4, 2]]
]
#############################################

iterator = 0  # Iterator pomocniczy
NumOfTasks = len(TasksPos)  # Liczba zadan
NumOfOperations = len(TasksPos[0])  # Liczba operacji #Czas ciaglego wykonywania dla jednej maszyny

# Obliczanie maksymalnego czsu wykonywania sie na maszynie
Cmax = 0
for operacje in range(NumOfOperations):
    Cmax += TasksPos[0][operacje][1]

# Generowanie listy z nazwami dla szerokosci Y
TasksWidth = [[0.0]*NumOfTasks for _ in range(2)]

for i in range(NumOfTasks):
    TasksWidth[i][0] = (i + 1) - 0.5 / 2
    TasksWidth[i][1] = 0.5

# Generowanie listy z nazwami dla wartosci Y
ListaZadan = []
for task in range(NumOfTasks + 1):
    ListaZadan.append("Zadanie " + str(task))

# Szerokosc i zakres X
xpos = np.arange(Cmax * NumOfTasks)
plt.xticks(xpos)

# Szerokosc i zakres Y
ypos = np.arange(NumOfTasks + 1)
plt.yticks(ypos, ListaZadan[0:NumOfTasks + 1])

# Ustawienie siatki
plt.grid(axis="x", alpha=0.5)

# Generowanie blokow
for szerokosc in TasksWidth:
    ax.broken_barh(TasksPos[iterator], szerokosc, facecolor="blue", edgecolor="0")
    iterator += 1

# Generowanie podpisow
for task in range(NumOfTasks):
    for operacja in range(NumOfOperations):
        label = "O" + str(operacja + 1)
        ax.text(TasksPos[task][operacja][0] + 0.1, task + 1, label)

plt.title("Diagram Gannta", fontsize=16)
fig.show()
