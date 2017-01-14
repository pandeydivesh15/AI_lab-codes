import sys

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
clean_data_file = dir_path + "en_clean_train_data.txt"
train_data_file_with_labels = dir_path + "en_train.txt"
test_data_file = dir_path + "en_test.txt"
test_data_labels_file = dir_path + "en_test_labels.txt"
data = []

with open(clean_data_file, "r") as file:
	for l in file:
		data.append(l)

limiter = int(0.8*(len(data)))
train_data = data[:limiter]
test_data = data[limiter:]

with open(train_data_file_with_labels, "w") as file1, open(test_data_file, "w") as file2, open(test_data_labels_file, "w") as file3:
	for l in train_data:
		file1.write(l)
	if not check:
		for l in test_data:
			temp = l.split()
			if temp:
				file2.write( temp[0] + '\n' )
				file3.write( temp[1] + '\n' )
	else:
		for l in test_data:
			file2.write(l)
