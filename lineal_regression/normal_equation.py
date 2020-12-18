from matplotlib import pyplot
import numpy as np
import csv

# Open file
data = np.genfromtxt('data/barcelona_apartments_training.csv', delimiter=',', skip_header=True)

# Create matrix and vector
y = data[:, 0]
X = data[:, 1:]

m = y.size #number of training examples

# Add column of 1s
X = np.concatenate([np.ones((m, 1)), X], axis=1)

theta = np.dot(np.dot(np.linalg.inv(np.dot(X.transpose(), X)), X.transpose()), y)

print(theta)

test = [1,1,1,56,1,0,0,0,0,0,0,0,0]
price = np.dot(test, theta)

print(price)

# Save the data in price_prediction
with open('../price_prediction/data/data.csv', 'w') as record_write:
    np.savetxt(record_write, np.asarray([theta]), delimiter=',')