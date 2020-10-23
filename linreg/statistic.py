import numpy as np
import statistics as st

def correlation(x_set, y_set):
	eq1 = np.dot(x_set, y_set) - sum(x_set) * sum(y_set) / len(x_set)
	eq2 = np.sqrt((sum([i ** 2 for i in x_set]) - sum(x_set) ** 2 / len(x_set)) \ 
	      * (sum([i ** 2 for i in y_set]) - sum(y_set) ** 2 / len(y_set)))
	return eq1 / eq2

def standard_deviation(arr : list) -> float:
	arr_mean = st.mean(arr)
	arr_lenght = len(arr)
	return np.sqrt((sum([(x - arr_mean) ** 2 for x in arr])) / (arr_lenght - 1))
