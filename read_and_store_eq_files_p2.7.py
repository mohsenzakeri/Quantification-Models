import pandas

eq_classes_file = open("/mnt/scratch2/mohsen/stan-test/parse_eq_classes_file/QuantificationModels/eq_classes.txt", "r")

#quant_file = pandas.read_table("/mnt/scratch2/mohsen/stan-test/salmon-0.11.3-linux_x86_64/sample_data/salmon-output/quant.sf",sep="\t")
quant_file = pandas.read_table("/mnt/scratch2/mohsen/stan-test/salmon-output/quant.sf",sep="\t")

effLens = quant_file['EffectiveLength']

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
	class_weights = list()
	wsum = 0.0
	for j in range(class_size):
		columns += [int(eq_class_info[j+1])+1]
		effLenProb = 1/effLens[int(eq_class_info[j+1])]
		class_weights += [float(eq_class_info[j+class_size+1])*effLenProb]
		wsum += class_weights[j]
		weights += [float(eq_class_info[j+class_size+1])]
	wnorm = 1.0/wsum
	for q in range(len(class_weights)):
		new_weight = class_weights[q]*wnorm
		#weights += [float(new_weight)]
	row_starts += [int(row_starts[i])+class_size]
	counts += [int(eq_class_info[-1])]

stan_data = { 'weights' : weights, 'columns' : columns, 'row_starts' : row_starts, 'counts' : counts, 'N' : len(counts), 'Q' : len(weights), 'M' : txps_count, 'alpha' : [1 for i in range(txps_count)]}

import pickle
pickle.dump( stan_data, open( "stan_data_large.p", "wb" ) )
