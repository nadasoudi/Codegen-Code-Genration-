import numpy as np

# Load the data
X = np.loadtxt('data-01-X.txt', delimiter=',')
y = np.loadtxt('data-01-y.txt', delimiter=',')

# Create a linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(X, y)

# Make predictions using the testing set
yhat = regr.predict(X)

# Calculate