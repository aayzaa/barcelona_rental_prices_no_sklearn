""" TODO """

import numpy as np

data = np.genfromtxt('../price_prediction/data/data.csv', delimiter=',')
theta = data[0]
mean = data[1]
standard_deviation = data[2]
print(theta)

# Open file
data = np.genfromtxt('data/barcelona_apartments.csv', delimiter=',', skip_header=True)
errors = 0

max_val = 5
apts = []

for row in data:
    test = row.copy()
    if test[0]/test[3] < max_val:
        apts.append(test.copy())
    test[0] = 1
    test[1] = (test[1] - mean[1]) / standard_deviation[1]
    test[2] = (test[2] - mean[2]) / standard_deviation[2]
    test[3] = (test[3] - mean[3]) / standard_deviation[3]
    price = np.dot(test, theta)
    errors += abs(price - row[0])

errors /= data.shape[0]
print(errors)
print(apts)