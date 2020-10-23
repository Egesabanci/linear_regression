import matplotlib.pyplot as plt

def plot_graph(x : list, y_true : list, predict : list,
	       x_label : str, y_label : str, title : str,
	       grid : bool, size : tuple):

	assert len(y_true) == len(predict)
	assert len(y_true) == len(x)

	plt.figure(figsize = size)
	plt.grid(grid)
	plt.title(title)
	plt.xlabel(x_label)
	plt.ylabel(y_label)
	plt.scatter(x = x, y = y_true, color = "blue")
	plt.scatter(x = x, y = predict, color = "red")
	plt.legend(labels = ["True Values", "Predicted Values"])
	plt.show()
