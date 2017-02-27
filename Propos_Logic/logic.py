import pandas as pd
import numpy as np

all_ops = ['!', '&', "|", ">", "~", "(", ")"]
ops_prior = {'!':5, '&':4, "|":3, ">":2, "~": 1, "(": 0, ")":0}

class Logic():
	def __init__(self, num_of_consts, num_of_statements):
		self.num_of_statements = num_of_statements
		self.num_of_consts = num_of_consts
		self.consts = [chr(i) for i in range(65, 65 + num_of_consts)]
		self.set_table()


	def set_table(self):
		temp = np.ndarray(
				  shape = [2**self.num_of_consts, self.num_of_consts], 
				  dtype = bool)
		decider = 2**(self.num_of_consts - 1)
		for x in range(0, self.num_of_consts):
			temp[:, x] = [(((y)/decider) % 2 == 0) for y in range(2**self.num_of_consts)]
			decider /= 2

		self.data = pd.DataFrame(temp, columns = self.consts)

	def view_table(self):
		return self.data

	def set_statements(self, statements_tuple):
		if len(statements_tuple) != self.num_of_statements:
			print "Error: Enter correct number of statements"
			return
		self.statements_tuple = statements_tuple

	def op_eval(self,op, a, b):
		if op == "!": return not b
		if op == "&": return (a and b)
		if op == "|": return (a or b)
		if op == ">":
			if a == True and b == False: return False
			return True
		if op == "~":
			if a == False and b == True: return False
			if a == True and b == False: return False
			return True

	def evaluate_row(self, row, expr):
		stack_consts = []
		stack_ops = []
		expr = list("(" + expr + ")")

		for ch in expr:
			if ch not in all_ops:
				stack_consts.append(self.data[ch][row]) # argument row used here
			else:
				if stack_ops:
					if ch == "(":
						stack_ops.append(ch)
					elif ch == ")":
						while stack_ops[-1] != "(":
							temp = stack_ops.pop()
							b = stack_consts.pop()
							if temp != '!':
								a = stack_consts.pop()
							else:
								a = None
							stack_consts.append(self.op_eval(temp, a, b))
						stack_ops.pop()
					else:
						while ops_prior[stack_ops[-1]] > ops_prior[ch]:
							temp = stack_ops.pop()
							b = stack_consts.pop()
							if temp != '!':
								a = stack_consts.pop()
							else:
								a = None
							stack_consts.append(self.op_eval(temp, a, b))
						stack_ops.append(ch)
				else:
					stack_ops.append(ch)
		return stack_consts.pop()


	def evaluate_statements(self):
		for x,y in self.statements_tuple:
			self.data[x] = [self.evaluate_row(i, y) for i in range(2**self.num_of_consts)]
		return

	def if_tautologies(self):
		tautologies = []
		for expr in self.statements_tuple:
			for value in self.data[expr[0]]:
				if value == False:
					break
			else:
				tautologies.append(expr)
		return tautologies

	def if_contradictions(self):
		contradictions = []
		for expr in self.statements_tuple:
			for value in self.data[expr[0]]:
				if value == True:
					break
			else:
				contradictions.append(expr)
		return contradictions

	def if_contingencies(self):
		contingencies = self.statements_tuple
		for x in self.if_contradictions():
			contingencies.remove(x)
		for x in self.if_tautologies():
			contingencies.remove(x)
		return contingencies

	def if_equivalences(self):
		equivalences = []
		for x in range(0, len(self.statements_tuple)):
			for y in range(x+1, len(self.statements_tuple)):
				if np.array_equal(self.data[self.statements_tuple[x][0]].values, 
								  self.data[self.statements_tuple[y][0]].values):
					equivalences.append((
						self.statements_tuple[x],
						self.statements_tuple[y]))
		return equivalences

	def if_logical_entailments(self):
		entailments = []
		for x in self.statements_tuple:
			for y in self.statements_tuple:
				if x == y:
					continue
				for i, j in zip(self.data[x[0]], self.data[y[0]]):
					if i == True and j == False:
						break
				else:
					if x != y:
						entailments.append((x,y))
		return entailments

	def if_consistent(self):
		check = np.array([True for i in range(len(self.statements_tuple))] , dtype = bool)
		for row in range(2**self.num_of_consts):
			if np.array_equal(
					check,
					self.data.loc[row,[x for x,y in self.statements_tuple]].values):
				print self.data.loc[row,[x for x,y in self.statements_tuple]].values
				print check
				return True
		return False





				
