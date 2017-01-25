
dir_path = "./"
train_file = dir_path + "train.txt"
test_file = dir_path + "test.txt"
train_file_hunPos = dir_path + "hunpos_train.txt"
test_file_hunPos = dir_path + "hunpos_test.txt"

with \
	open(train_file, 'r') as file1,\
	open(test_file, 'r') as file2, \
	open(train_file_hunPos, "w") as write_to1, \
	open(test_file_hunPos, "w") as write_to2:

	for l1 in (l.rstrip() for l in file1):
		temp1 = l1.split()
		if temp1:
			write_to1.write(temp1[0] + "\t" + temp1[2] + '\n')
		else:
			write_to1.write('\n')

	for l2 in (l.rstrip() for l in file2):
		temp2 = l2.split()
		if temp2:
			write_to2.write(temp2[0] + '\n')
		else:
			write_to2.write('\n')


