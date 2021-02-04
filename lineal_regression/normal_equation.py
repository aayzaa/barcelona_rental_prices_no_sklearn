""" Performs the normal equation on the data.

The goal of this project was to implement lineal regression,
    but here I added the normal equation operation in order
    to check if both arrived at the same results.
    Even though theta is different, due to the normalization
    of features in the multilineal regression, both presents
    the same results when tested against data.

(CC) 2020 Alex Ayza, Barcelona, Spain
alexayzaleon@gmail.com
"""

from matplotlib import pyplot
import numpy as np
import csv

# Open file
data = np.genfromtxt('data/barcelona_apartments_training.csv', delimiter=',', skip_header=True)

# Create matrix and vector
y = data[:, 0]
X = data[:, 1:]

# Number of training examples
m = y.size

# Add column of 1s
X = np.concatenate([np.ones((m, 1)), X], axis=1)

# Normal equation
theta = np.dot(np.dot(np.linalg.inv(np.dot(X.transpose(), X)), X.transpose()), y)

# Save the data in price_prediction
with open('../price_prediction/data/data.csv', 'w') as record_write:
    np.savetxt(record_write, np.asarray([theta]), delimiter=',')
