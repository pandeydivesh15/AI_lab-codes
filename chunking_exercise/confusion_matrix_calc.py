import sys
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report

if len(sys.argv) != 2:
	print("Enter the model option.")
	exit()
if sys.argv[1] == "--hunpos":
	check = 0;
elif sys.argv[1] == "--crf++":
	check = 1
else:
	print "Enter correct option."
	exit()

dir_path = "./"

if not check:
	test_data_labels_file = dir_path + "test.txt"
predicted_labels_file = dir_path + "chunking_result.txt"


labels = set()
predicted_labels = []
test_data_labels = []

if not check:
	with open(test_data_labels_file, "r") as file1, open(predicted_labels_file, "r") as file2:
		for line in (l.rstrip() for l in file1):
			temp = line.split()
			if temp:
				test_data_labels.append(temp[2])
				labels.add(temp[2])
		for line in (l.rstrip() for l in file2):
			if line:
				predicted_labels.append(line.split()[1])
else:
	with open(predicted_labels_file, "r") as file:
		for line in (l.rstrip() for l in file):
			if line:
				predicted_labels.append(line.split()[3])
				test_data_labels.append(line.split()[2])
				labels.add(line.split()[2])

labels = sorted(list(labels))

predicted_labels = np.array(predicted_labels)
test_data_labels = np.array(test_data_labels)

simple_conf_matrix = confusion_matrix(test_data_labels,predicted_labels)

conf_matrix = pd.DataFrame(columns = labels, index = labels)


for x,y in zip(simple_conf_matrix,labels):
	conf_matrix[y] = x
conf_matrix = conf_matrix.transpose()
print conf_matrix
print "Classification Report: " + classification_report(test_data_labels, predicted_labels)