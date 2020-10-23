import numpy as np 
import statistics as st

from metrics import MSE, MAE
from statistic import correlation, standard_deviation

class LinearRegressor(object):

	def fit(self, x_train, y_train):
		self.x_train = x_train
		self.y_train = y_train
		assert len(x_train) == len(y_train)

		mx = st.mean(self.x_train) 
		my = st.mean(self.y_train)
		sx = standard_deviation(self.x_train)
		sy = standard_deviation(self.y_train)
		
		self.b1 = correlation(self.x_train, self.y_train) * (sy / sx)
		self.b0 = my - (self.b1 * my)

	def loss(self, pred_list, true_list):
		preds = [self.b0 + self.b1 * i for i in pred_list] # pred_list = x_train for prediction
		self.error = MSE(true_list, preds) # error metric of the model (according to train sets)
		return np.sqrt(self.error)

	def predict(self, value):
		self.model_loss = np.sqrt(self.loss(self.x_train, self.y_train))
		return (self.b0 + self.b1 * value) + self.model_loss # final prediction