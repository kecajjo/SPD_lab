

def read_from_file(file_name):
    f = open(file_name, "r")

    line_from_file = f.readline()

    list_from_file = line_from_file.split(" ")
    number_of_task = int(list_from_file[0])
    number_of_machine = int(list_from_file[1])


    loaded_table_from_file = []

    for i in range(number_of_task):
        row = []
        line_from_file = f.readline()
        list_from_file = line_from_file.split(" ")
        for j in range(number_of_machine):
            row.append(int(list_from_file[j]))
        loaded_table_from_file.append(row)
    return number_of_task, number_of_machine, loaded_table_from_file

def create_csv_file(name_of_file):
    f = open(name_of_file,"x")
    f.write("Size of instance;Algorithm;Cmax;Executing time\n")
    f.close()


def append_to_file(name_of_file,row):
    f = open(name_of_file,"a")
    f.write(row)
    f.write("\n")

def format_data_to_string(number_of_tasks, number_of_machines,algorithm_type_in_string,tasks_order,cmax,duration):
    return_string1 = "{}".format(number_of_tasks) + "x{}".format(number_of_machines) +"  ;   "+algorithm_type_in_string + "  ;   "
    return_string2 = "{}".format(tasks_order) + "   ;   {}".format(cmax) + "  ;   {}".format(duration)

    return  return_string1+return_string2
