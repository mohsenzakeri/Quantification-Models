eq_classes_file = open("/mnt/scratch2/mohsen/stan-test/parse_eq_classes_file/QuantificationModels/eq_classes_small.txt", "r")

txps_count = int(eq_classes_file.readline())

eq_classes_count = int(eq_classes_file.readline())

txps = list()
for i in range(txps_count):
    txps += [eq_classes_file.readline().rstrip()]

weights = list()
columns = list()
row_starts = list()
counts = list()

row_starts += [1]
for i in range(eq_classes_count):
    eq_class_info = eq_classes_file.readline().split()
    class_size = int(eq_class_info[0])
    for j in range(class_size):
        columns += [int(eq_class_info[j+1])+1]
        weights += [float(eq_class_info[j+class_size+1])]
    row_starts += [int(row_starts[i])+class_size]        
    counts += [int(eq_class_info[-1])]


stan_data = { 'weights' : weights, 'columns' : columns, 'row_starts' : row_starts, 'counts' : counts, 'N' : len(counts), 'Q' : len(weights), 'M' : txps_count, 'alpha' : [1 for i in range(txps_count)]}

import pickle
pickle.dump( stan_data, open( "stan_data_small.p", "wb" ) )
