import re

data_format= re.compile(
    r"(?P<sr_num>[\d]+)\s"
    r"(?P<word>\S*)\s"
    r"(?P<no_use1>\S*)\s"
    r"(?P<tag>\S*)\s"
    r"(?P<no_use2>.*)"
)

dir_path = "./"
path_to_file = dir_path + "en-ud-train.conllu"
clean_data_file = dir_path + "en_clean_train_data.txt"

with open(path_to_file, "r") as file, open(clean_data_file, "w") as write_to:
	for line in (l.rstrip() for l in file):
		match = data_format.match(line)
		if match:
			mydict = match.groupdict()
			word = mydict["word"]
			tag = mydict["tag"]
			write_to.write(word + '\t' + tag + '\n')
		else:
			if not line:
				write_to.write('\n')
			
