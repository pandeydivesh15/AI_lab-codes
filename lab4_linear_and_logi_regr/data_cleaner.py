import numpy as np

def get_data(model):
	if model == "logistic":
		check = 1
	elif model == "linear":
		check = 0
	else:
		print "Enter correct option."
		exit()

	if check:
		data_file = "./diabetes.arff"
	else:
		data_file= "./dataset_2"

	x, y = [], [] 
	with open(data_file, "r") as file:
		for line in file:
			l = line.strip()
			if l:
				if l[0] == '@' or l[0] == '%':
					continue
				temp = l.split(',')
				if check:
					sample_dict = { "tested_positive" : 1, "tested_negative": 0}
					y.append(sample_dict[temp[-1]])
					x.append(temp[:-1])
				else:
					y.append(temp[-1])
					x.append(temp[:-1])

	limiter = int(.8 * len(y))
	x_train = np.array(x[:limiter], float)
	x_test = np.array(x[limiter:], float) 
	y_train = np.array(y[:limiter], float)
	y_test = np.array(y[:limiter], float)

	return x_train, y_train, x_test, y_test