""" Holds the class used to predict prices.

(CC) 2020 Alex Ayza, Barcelona, Spain
alexayzaleon@gmail.com
"""

import numpy as np

class PricePrediction:
    """Class used to predict the prices of apartments."""

    # This hashtable translates an area into an index of the matrix
    area_translation = {"eixample": 4, "ciutat_vella": 5, "gracia": 6, "horta_guinardo": 7, "les_corts": 8,
                        "nou_barris": 9, "sant_andreu": 10, "sant_marti": 11, "sants_montjuic": 12,
                        "sarria_sant_gervasi": "sarria_sant_gervasi"}

    def __init__(self):
        """Initializes the predictor with the current data."""
        data = np.genfromtxt('price_prediction/data/data.csv', delimiter=',')
        self.theta = data[0]
        self.mean = data[1]
        self.standard_deviation = data[2]

    def predict_price(self, rooms, bathrooms, sizem2, area):
        """Predicts the price of one apartment.

        :param rooms: Number of rooms.
        :param bathrooms: Number of bathrooms.
        :param sizem2: Size in squared meters.
        :param area: Area of Barcelona where it is located.
        :return: A float representing the predicted price.
        """

        apartment = [1, rooms, bathrooms, sizem2, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        area_code = self.area_translation[area]
        if area_code != "sarria_sant_gervasi":
            # Sarria-Sant-Gervasi is represented by the omission of 1s
            apartment[area_code] = 1

        # Normalizes the rooms, bathrooms and sizem2 features
        apartment[1] = (apartment[1] - self.mean[1]) / self.standard_deviation[1]
        apartment[2] = (apartment[2] - self.mean[2]) / self.standard_deviation[2]
        apartment[3] = (apartment[3] - self.mean[3]) / self.standard_deviation[3]

        price = np.dot(apartment, self.theta)
        return round(price, 2)
