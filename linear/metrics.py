import statistics as st

def MSE(y_true, y_pred):
	return st.mean([(y_true[x] - y_pred[x]) ** 2 for x in range(len(y_true))])

def MAE(y_true, y_pred):
	return st.mean([abs(y_true[x] - y_pred[x]) for x in range(len(y_true))])
