import numpy as np
from sklearn import preprocessing
from sklearn.metrics import mean_squared_error, classification_report, confusion_matrix
from math import sqrt

def sigmoid(z):
    return 1.0/(1.0+np.exp(-z))

class Linear_reg():
	def __init__(self, num_of_features):
		self.name = "Linear_reg"
		self.parameters = np.random.normal(0,1,num_of_features+1)

	def hypo(self, features):
		return np.dot(np.insert(features,0,1), self.parameters)

	def cost_func(self, all_data_items, actual_y_values):
		ans = 0.0
		for features, y in zip(all_data_items, actual_y_values):
			ans += (self.hypo(features) - y)**2
		return ans/(2*len(all_data_items))

	def find_gradient(self, data_values, y_values, i):
		temp = 0.0
		for x,y in zip(data_values, y_values):
			if i == 0:
				temp += 1 * (self.hypo(x) - y)
			else:
				temp += x[i-1] * (self.hypo(x) - y)
		return temp / len(data_values)
	def prediction_report(self, y_pred, y_true):
		print "Root Mean Square Error in Linear regression is", \
			sqrt(mean_squared_error(y_pred, y_true))

class Logistic_reg():
	def __init__(self, num_of_features):
		self.name = "Logistic_reg"
		self.parameters = np.random.normal(0,1,num_of_features+1)
		self.threshold = 0.25;

	def hypo(self, features):
		return sigmoid(np.dot(np.insert(features,0,1), self.parameters))

	def cost_func(self, all_data_items, actual_y_values):
		ans = 0.0
		for features, y in zip(all_data_items, actual_y_values):
			temp = self.hypo(features)
			ans += (y*np.log(temp) + (1-y)*np.log(1-temp))
		return -1*ans/(len(all_data_items))

	def find_gradient(self, data_values, y_values, i):
		temp = 0.0
		for x,y in zip(data_values, y_values):
			h = self.hypo(x)
			if i == 0:
				temp += 1 * (h - y) / (h * (1 - h)) 
			else:
				temp += x[i-1] * (h - y) / (h * (1 - h))
				
		return temp / len(data_values)

	def check_threshold(self, y):
		return (1.0 if y > self.threshold else 0.0)

	def prediction_report(self, y_pred, y_true):
		print "Report for Logistic Regression: "
		# self.threshold = np.mean([x*y for x,y in zip(y_pred,y_true)])
		# print self.threshold
		y_pred = [self.check_threshold(y) for y in y_pred]
		print classification_report(y_true, y_pred)
		print confusion_matrix(y_true, y_pred)


		
class Regression_model():

	def __init__(self, regr_model, num_of_features):
		self.model = regr_model(num_of_features)

	def train(self, all_data_items, actual_y_values, l_rate, mini_batch_size, epochs):
		num_of_iterations = len(all_data_items) / mini_batch_size

		all_data_items = all_data_items.transpose()
		scaled_data_items = np.array([preprocessing.scale(x) for x in all_data_items])
		scaled_data_items = scaled_data_items.transpose()
		scaled_y_values = actual_y_values

		for e in range(0,epochs):
			splitter = 0
			for i in range(0, num_of_iterations):
				data_values = scaled_data_items[splitter : (splitter + mini_batch_size)]
				y_values = scaled_y_values[splitter : (splitter + mini_batch_size)]	
				splitter += mini_batch_size

				num = len(self.model.parameters);
				update_values = np.zeros(num)
				for j in range(0,num):
					update_values[j] = self.model.find_gradient(data_values, y_values, j)
				
				self.model.parameters -= l_rate * update_values
				
				print "Iteration ", i
				print "Current Cost: ", self.model.cost_func(scaled_data_items, scaled_y_values)
			print "Epoch ", e+1, " 	Complete"

		print "Training Done"

	def test(self, all_data_items, actual_y_values):
		all_data_items = all_data_items.transpose()
		scaled_data_items = np.array([preprocessing.scale(x) for x in all_data_items])
		scaled_data_items = scaled_data_items.transpose()
		scaled_y_values = actual_y_values		

		y_pred = []
		y_true = []
		for x,y in zip(scaled_data_items, scaled_y_values):
			y_pred.append(self.model.hypo(x))
			y_true.append(y)
		
		self.model.prediction_report(y_pred, y_true)


