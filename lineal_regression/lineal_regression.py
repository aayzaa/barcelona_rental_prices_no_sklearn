from matplotlib import pyplot
import numpy as np
import csv


def normalize_values(matrix, cols_to_normalize):
    new_matrix = matrix.copy()
    mean = np.zeros(matrix.shape[1])
    deviation = np.zeros(matrix.shape[1])

    for column in range(matrix.shape[1]):
        if column in cols_to_normalize:
            mean[column] += np.mean(new_matrix[:, column])
            deviation[column] += np.std(new_matrix[:, column])

            new_matrix[:, column] -= mean[column]
            new_matrix[:, column] /= deviation[column]

    return new_matrix, mean, deviation


def computeCostMulti(X, y, theta):
    # Initialize some useful values
    m = y.shape[0]  # number of training examples

    # You need to return the following variable correctly
    J = 0

    # ======================= YOUR CODE HERE ===========================
    hypothesis = np.dot(X, theta)
    J = np.dot(hypothesis - y, hypothesis - y) / (2 * m)
    # ==================================================================
    return J


def gradient_descent(X, y, theta, alpha, iterations):
    # Initialize some useful values
    m = y.shape[0]  # number of training examples

    # make a copy of theta, which will be updated by gradient descent
    theta = theta.copy()

    J_history = []

    for i in range(iterations):
        # ======================= YOUR CODE HERE ==========================
        theta = theta - (alpha / m) * (np.dot(X, theta) - y).dot(X)
        # =================================================================

        # save the cost J in every iteration
        J_history.append(computeCostMulti(X, y, theta))

    return theta, J_history


# Open file
data = np.genfromtxt('data/barcelona_apartments_training.csv', delimiter=',', skip_header=True)

# Create matrix and vector
y = data[:, 0]
X = data[:, 1:]

m = y.size #number of training examples

#normalize values
columns_to_normalize = [0, 1, 2]
X, mean, standard_deviation = normalize_values(X, columns_to_normalize)

# Add column of 1s
X = np.concatenate([np.ones((m, 1)), X], axis=1)

# START GRADIENT DESCENT
alpha = 0.3
iterations = 10000

theta = np.zeros(X.shape[1])
theta, J_history = gradient_descent(X, y, theta, alpha, iterations)

print(theta)

test = [1,1,1,56,1,0,0,0,0,0,0,0,0]
test[1] = (test[1] - mean[0]) / standard_deviation[0]
test[2] = (test[2] - mean[1]) / standard_deviation[1]
test[3] = (test[3] - mean[2]) / standard_deviation[2]
price = np.dot(test, theta)

print(price)


print(mean)
print(standard_deviation)

mean = np.insert(mean, 0, 0)
standard_deviation = np.insert(standard_deviation, 0, 0)

# Save the data in price_prediction
with open('../price_prediction/data/data.csv', 'w') as record_write:
    np.savetxt(record_write, np.asarray([theta]), delimiter=',')
    np.savetxt(record_write, np.asarray([mean]), delimiter=',')
    np.savetxt(record_write, np.asarray([standard_deviation]), delimiter=',')







