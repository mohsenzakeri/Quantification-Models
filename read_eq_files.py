import csv

def read_eq_classes_file(file_name):
    eq_classes_file = open(file_name, "r")
    
    txps_count = int(eq_classes_file.readline())
    eq_classes_count = int(eq_classes_file.readline())

    txps = list()
    for i in range(txps_count):
        txps += [eq_classes_file.readline().rstrip()]

    print(txps_count)
    print(eq_classes_count)
    print(len(txps))
    print(txps[0])

    weights = list()
    columns = list()
    row_starts = list()
    counts = list()
    
    row_starts += [1]
    for i in range(eq_classes_count):
        eq_class_info = eq_classes_file.readline().split()
        class_size = int(eq_class_info[0])
        for j in range(class_size):
            columns += [int(eq_class_info[j+1])]
            weights += [float(eq_class_info[j+class_size+1])]
        row_starts += [int(row_starts[i])+class_size]        
        counts += [int(eq_class_info[-1])]

    print(len(weights))
    print(len(columns))
    print(len(row_starts))
    print(len(counts))

    #with open("weights.csv", 'w', newline='') as myfile:
    #    wr = csv.writer(myfile)
    #    wr.writerow(weights)

    #with open("columns.csv", 'w', newline='') as myfile:
    #    wr = csv.writer(myfile)
    #    wr.writerow(columns)

    #with open("row_starts.csv", 'w', newline='') as myfile:
    #    wr = csv.writer(myfile)#, quoting=csv.QUOTE_ALL)
    #    wr.writerow(row_starts)

    with open("counts.csv", 'w', newline='') as myfile:
        wr = csv.writer(myfile)#, quoting=csv.QUOTE_ALL)
        wr.writerow(counts)


def main():
    read_eq_classes_file("eq_classes.txt")   

if __name__=="__main__":
    main()
