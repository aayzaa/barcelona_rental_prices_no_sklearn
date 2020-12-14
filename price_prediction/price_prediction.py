import numpy as np

class PricePrediction:

    area_translation = {"eixample": 4, "ciutat_vella": 5, "gracia": 6, "horta_guinardo": 7, "les_corts": 8,
                        "nou_barris": 9, "sant_adreu": 10, "sant_marti": 11, "sants_montjuic": 12,
                        "sarria_sant_gervasi": "sarria_sant_gervasi"}

    def __init__(self):
        data = np.genfromtxt('price_prediction/data/data.csv', delimiter=',')
        self.theta = data[0]
        self.mean = data[1]
        self.standard_deviation = data[2]

    def predict_prize(self, rooms, bathrooms, sizem2, area):
        apartment = [1, rooms, bathrooms, sizem2, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        area_code = self.area_translation[area]
        if area_code != "sarria_sant_gervasi":
            apartment[area_code] = 1

        apartment[1] = (apartment[1] - self.mean[1]) / self.standard_deviation[1]
        apartment[2] = (apartment[2] - self.mean[2]) / self.standard_deviation[2]
        apartment[3] = (apartment[3] - self.mean[3]) / self.standard_deviation[3]
        price = np.dot(apartment, self.theta)
        return price
