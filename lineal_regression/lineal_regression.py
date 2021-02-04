""" Performs a multilineal regression calculation on the cleaned data.

The operation is done with a gradient descent, since I wanted to
    practice this technique.

(CC) 2020 Alex Ayza, Barcelona, Spain
alexayzaleon@gmail.com
"""

from matplotlib import pyplot
import numpy as np
import csv

def normalize_values(matrix, cols_to_normalize):
    """ Normalizes values to be between -1 and 1.

    :param matrix: Matrix to be normalized.
    :param cols_to_normalize: Index of the columns that need to be normalized.
    :return: A normalized matrix, a vector with the means of the normalized
        variables, and a vector with the means of the standard deviation.
    """

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


def gradient_descent(X, y, theta, alpha, iterations):
    """ Performs gradient descent with the X matrix and the y vector.

    :param X: Matrix with the features of the multilinear regression.
    :param y: Vector with the results of each row.
    :param theta: Result of the regression at each step.
    :param alpha: Factor that modifies how quickly the algorithm converges.
    :param iterations: Number of iterations to be performed.
    :return: Theta, the result vector that indicates the weight of each feature.
    """

    # Get the number of training examples
    m = y.shape[0]
    theta_cpy = theta.copy()

    # Repeats gradient descent until the number of iterations have happened
    for i in range(iterations):
        theta_cpy = theta_cpy - (alpha / m) * (np.dot(X, theta_cpy) - y).dot(X)

    return theta_cpy


# Open file
data = np.genfromtxt('data/barcelona_apartments.csv', delimiter=',', skip_header=True)

# Create matrix and vector
y = data[:, 0]
X = data[:, 1:]

# Number of training examples
m = y.size

# Normalize values (rooms, bathrooms, sizem2)
columns_to_normalize = [0, 1, 2]
X, mean, standard_deviation = normalize_values(X, columns_to_normalize)

# Add column of 1s at the start
X = np.concatenate([np.ones((m, 1)), X], axis=1)

# Perform gradient descent
alpha = 0.3
iterations = 10000
theta = np.zeros(X.shape[1])
theta = gradient_descent(X, y, theta, alpha, iterations)

# Prepare data to be stored
mean = np.insert(mean, 0, 0)
standard_deviation = np.insert(standard_deviation, 0, 0)

# Save the data in price_prediction
with open('../price_prediction/data/data.csv', 'w') as record_write:
    np.savetxt(record_write, np.asarray([theta]), delimiter=',')
    np.savetxt(record_write, np.asarray([mean]), delimiter=',')
    np.savetxt(record_write, np.asarray([standard_deviation]), delimiter=',')







