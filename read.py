def read_from_file(file_name):
    f = open(file_name, "r")

    lineFromFile = f.readline()

    listFromFile = lineFromFile.split(" ")
    numberOfTask = int(listFromFile[0])
    numberOfMachine = int(listFromFile[1])


    matrix = []

    for i in range(numberOfTask):
        row = []
        lineFromFile = f.readline()
        listFromFile = lineFromFile.split(" ")
        for j in range(numberOfMachine):
            row.append(int(listFromFile[j]))
        matrix.append(row)
    print(matrix)
    return numberOfTask, numberOfMachine, matrix