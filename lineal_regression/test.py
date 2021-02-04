""" File used to calculate statistics and perform tests over the predictions.

I used this file to find the average error in €uros in different price ranges,
    and to find apartments with logic input errors (10€ for a 200 m2 apartment,
    or houses with 20000 m2).

(CC) 2020 Alex Ayza, Barcelona, Spain
alexayzaleon@gmail.com
"""

import numpy as np

data = np.genfromtxt('../price_prediction/data/data.csv', delimiter=',')
theta = data[0]
mean = data[1]
standard_deviation = data[2]
print(theta)

# Open file
data = np.genfromtxt('data/barcelona_apartments.csv', delimiter=',', skip_header=True)
errors = 0

# Price/m2 ratio used to find outlier apartments
max_val = 6
apts = []

for row in data:
    test = row.copy()
    if test[0]/test[3] < max_val:
        # If the ratio is inferior (sometimes I used superior) save it to manually check.
        apts.append(test.copy())

    test[0] = 1
    test[1] = (test[1] - mean[1]) / standard_deviation[1]
    test[2] = (test[2] - mean[2]) / standard_deviation[2]
    test[3] = (test[3] - mean[3]) / standard_deviation[3]
    price = np.dot(test, theta)

    # Adds the error on the price calculation
    errors += abs(price - row[0])

errors /= data.shape[0]
print(errors)
print(apts)
