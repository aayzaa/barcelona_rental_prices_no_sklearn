import numpy as np

theta = [1618.49529167, -90.80193226, 295.69729505, 753.92555624, -29.20083511, -149.00956607, -200.28646299,
         -334.86077178, -175.65009037, -395.36695407, -383.24034774, -56.68956142, -257.86113986]

mean = [2.49412021, 1.53070557, 91.63697735, 0, 0, 0, 0, 0, 0, 0, 0, 0]
standard_deviation = [1.11470231, 0.72108466, 62.9399184, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Open file
data = np.genfromtxt('data/barcelona_apartments.csv', delimiter=',', skip_header=True)
errors = 0

for row in data:
    test = row.copy()
    test[0] = 1
    test[1] = (test[1] - mean[0]) / standard_deviation[0]
    test[2] = (test[2] - mean[1]) / standard_deviation[1]
    test[3] = (test[3] - mean[2]) / standard_deviation[2]
    price = np.dot(test, theta)
    print(str(price) + " - " + str(row[0]) + " ERROR: " + str(abs(price - row[0])))
    errors += abs(price - row[0])

errors /= data.shape[0]
print(errors)