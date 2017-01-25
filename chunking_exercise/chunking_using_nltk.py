from nltk import RegexpParser

dir_path  = "./"
result_file_hunPos = dir_path + "test.txt"
final_result = dir_path + "chunking_result.txt"

words_and_tags = []

with open(result_file_hunPos, 'r') as file:
	for l in file:
		temp = l.split()
		if temp:
			words_and_tags.append((temp[0], temp[1]))

grammar = r"""NP: {<DT>?<JJ>*<NN>} #Simple noun phrase chunking
			  MyChunk: {<RB.?>*<VB.?>*<NNP>+<NN>?} #Sample chunking format 
			  """

cp = RegexpParser(grammar)

result = cp.parse(words_and_tags)	
print result
# with open(final_result, 'w') as file:
# 	for i 

