import re
from copy import deepcopy

HEAD_RULES = {
	"VP": "V",
	"NP": "N",
	"S": "VP",
	"ROOT": "S",
	"PP": "NP",	
}


# A very basic Karaka chart for active voice. 
KARAKA_CHART = {
	"subj"		: "Karta (K1)",
	"obj"		: "Karam (K2)",
	"prep+to"	: "Sampradan (K4)",
	"prep+by"	: "Apadaan (K5)",
	"prep+in"	: "Adhikaran (K7place)",
	"prep+at"	: "Adhikaran (K7time)"
}

# For storing karaka relations encountered in the sentence.
RELATIONS = {} 

# def __init__(self, data, children=[], head=""):
# 		self.data = data
# 		self.children = children
# This created problems, n2.children.append() was also appending to n1.children

class Treenode():
	def __init__(self, data):
		self.data = data
		self.children = []
		self.head = ""

	def add_child(self, node):
		self.children.append(node)

	def set_head(self, head):
		self.head = head

	def find_head(self):
		for x in self.children:
			if re.match(HEAD_RULES[self.data], x.data):
				self.head = x.head
				# break

	def __str__(self):
		return str(self.data) + " (head: " + str(self.head) + ")"

def read_PST(elements):
	elements = elements[1:-1]
	stack = []
	prev_x = None

	for x in elements:
		if x == "(":
			pass
		elif x != ")":
			node = Treenode(x)
			stack.append(node)
		else:
			if prev_x != ")":
				n1 = stack.pop()
				n1.set_head(n1.data)
				n2 = stack.pop()
				n2.children.append(n1)
				n2.set_head(n1.data)
				n3 = stack.pop()
				n3.add_child(n2)
				stack.append(n3)
			else:
				n1 = stack.pop()
				n1.find_head()
				n2 = stack.pop()
				n2.add_child(n1)
				stack.append(n2)

		prev_x = x[:]

	n = stack.pop()
	n.find_head()
	return n



def get_relations(PST_root):
	for x in PST_root.children:
		if x.data == "NP":
			RELATIONS[PST_root.head + x.head] = "subj"
		if x.data == "VP":
			for y in x.children:
				if y.data == "NP":
					RELATIONS[x.head + y.head] = "obj"
				if y.data == "PP":
					RELATIONS[x.head + y.head] = "prep+" + y.children[0].head 


def traverse_tree(root):
	print root
	for x in root.children:
		traverse_tree(x)

def show_simple_Dtree(root):
	for x in root.children:
		print root.data + " ----> " + x.data
		show_simple_Dtree(x)
	
def show_Dtree(root):
	for x in root.children:
		try:
			print root.data + " ----> " + x.data + \
			" (Karaka Relation: %s)" % KARAKA_CHART[RELATIONS[root.data + x.data]]
		except:
			print root.data + " ----> " + x.data
		show_Dtree(x)

# Lets start building Dependency tree, merging common heads
def merge_heads(root):
	if not root.children:
		return
	for x in root.children:
		merge_heads(x)
	for x in root.children:
		if x.head == root.head:
			root.children.remove(x)
			root.children.extend(x.children)
			root.data = x.data
			break

if __name__ == '__main__':
	with open("PST.txt", "r") as file:
		data = " ".join(file.read().split())
		data = data.replace("(", "( ")
		data = data.replace(")", " )")
		data = data.split()

	PST_root = read_PST(data)

	print "Showing Phrase Structure Tree with Heads\n"
	traverse_tree(PST_root)
	
	root = deepcopy(PST_root)
	merge_heads(root)

	print "\nShowing Simple Dependency Tree without Karaka relations\n"
	show_simple_Dtree(root)

	get_relations(PST_root.children[0]) # ROOT -> S = PST_root.children[0]
	# print RELATIONS
	print "\nShowing Dependency Tree with Karaka relations\n"
	show_Dtree(root)






