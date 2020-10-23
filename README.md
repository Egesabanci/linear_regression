# Linear Regression Module

Very basic, simple and comfortable "Linear Regressor" with couple lines of code...

### Installation
```
pip install linreg
```

### Usage

```python
# import Linear Regressor
from linreg import LinearRegressor

# sample data
x_train = numpy.array
y_train = numpy.array

# create model and fit with data
model = LinearRegressor()
model.fit(x_train, y_train)
```

### Plot Model
```python
# import plot function
from linreg import plot_graph

# sample test data
x_test = numpy.array
y_test = numpy.array

# plot the graph
plot_graph(x_test, y_test, [model.predict(x) for x in x_test],
		   x_label = "Sample X", y_label = "Sample Y", title = "Test",
		   grid = True, size = (10, 5))
```