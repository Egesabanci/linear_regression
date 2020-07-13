import random
import numpy as np

sample_set = [x for x in range(75)]
dec_inc = [random.uniform(-10, 10) for _ in range(10)]

# sample train and test set
x_train = [i + random.choice(dec_inc) for i in sample_set]
y_train = [i + random.choice(dec_inc) for i in sample_set]

x_test = [i + random.choice(dec_inc) for i in sample_set]
y_test = [i + random.choice(dec_inc) for i in sample_set]

# create model
from linear import LinearRegressor
from metrics import MSE # from metrics.py

model = LinearRegressor() # from linear.py
model.fit(x_train, y_train)

print("MODEL COEF:", model.b1,
	  "\nMODEL INTERCEPT:", model.b0,
	  "\nMODEL LOSS:", np.sqrt(MSE(y_test, [model.predict(x) for x in x_test])))
	  # model loss: according to the test sets

# plot the model with test sets
from plot import plot_graph # from plot.py
plot_graph(x_test, y_test, [model.predict(x) for x in x_test],
		   x_label = "Sample X", y_label = "Sample Y", title = "Test",
		   grid = True, size = (10, 5))
