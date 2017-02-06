import numpy as np
import pandas as pd

class Hmm_model(object):
	def __init__(self, file_loc):
		self.train_data_file = file_loc

	def measure_probabilites(self):
		self.state_trans_prob = pd.DataFrame(
									data = 0,
									index = self.tags,
									columns = self.tags)
		self.emission_prob = pd.DataFrame(
									data = 0,
									index = self.tags,
									columns = self.words)
		self.prior_prob= pd.DataFrame(
									data = 0,
									index = self.tags,
									columns = ["PriorProb"])

		previous_tag = ''
		with open(self.train_data_file, 'r') as file:
				for line in (l.rstrip() for l in file):
					temp = line.split()
					if temp:
						if not previous_tag:
							self.prior_prob['PriorProb'][temp[1]] += 1
							previous_tag = temp[1]
						self.emission_prob[temp[0]][temp[1]] += 1
						self.state_trans_prob[temp[1]][previous_tag] += 1
						previous_tag = temp[1]
					else:
						previous_tag = ''
		self.emission_prob = self.emission_prob / self.emission_prob.sum()
		self.state_trans_prob = self.state_trans_prob / self.state_trans_prob.sum()
		self.prior_prob = self.prior_prob / self.prior_prob.sum()

	def train(self):
		temp_set1 = set()
		temp_set2 = set()
		with open(self.train_data_file, 'r') as file:
			for line in (l.rstrip() for l in file):
				temp = line.split()
				if temp:
					temp_set1.add(temp[0])
					temp_set2.add(temp[1])
		
		self.words = sorted(list(temp_set1))
		self.tags = sorted(list(temp_set2))

		self.measure_probabilites()

	def find_max_prob(self, sliced_array, final_tag):
		maxm_prob = 0.0
		index = 0
		for i in range(len(sliced_array)):
			temp = sliced_array[i] * self.state_trans_prob[final_tag][self.tags[i]]
			if maxm_prob < temp:
				maxm_prob = temp
				index = i
		return maxm_prob, index
			
		

	def viterbi(self, all_words):
		predicted_tags = []

		l = len(all_words)
		k = len(self.tags)

		T1 = np.zeros([k,l])
		T2 = np.zeros([k,l] , int)

		for index, tag in zip(range(k), self.tags):
			T1[index][0] = self.prior_prob['PriorProb'][tag] * self.emission_prob[all_words[0]][tag]

		for pos in range(1,l):
			for index, tag in zip(range(k), self.tags):
				maxm_prob, tag_index = self.find_max_prob(T1[:,pos-1], tag)
				T1[index, pos] = maxm_prob * self.emission_prob[all_words[pos]][tag]
				T2[index, pos] = tag_index

		ans_tag_index = np.argmax(T1[:,-1])
		predicted_tags.append(self.tags[ans_tag_index])

		for i in range(l-1):
			ans_tag_index = T2[ans_tag_index][l-i-1]
			predicted_tags.append(self.tags[ans_tag_index])
		predicted_tags = predicted_tags[::-1]
		return predicted_tags

	def tag_sentence(self, data):
		all_words = data.strip().split()
		tags = self.viterbi(all_words)

		print pd.DataFrame(data = [all_words, tags], index = ["Words", "Tags"])


if __name__ == '__main__':
	h = Hmm_model("train.txt")
	h.train()
	h.tag_sentence("preacher near the mosque killed the terrorist man living next to Syrian border in Baghdad .")