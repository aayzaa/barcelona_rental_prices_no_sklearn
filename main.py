from price_prediction.price_prediction import PricePrediction

def main():
    predictor = PricePrediction()

    print("This program predicts the rent price of a Barcelona apartment.")
    print("Type the information requested to get a prediction. Type /'exit/' at any point to stop the program.")

    while(True):
        rooms = input("Rooms: ")
        if rooms == "exit": exit()

        bathrooms = input("Bathrooms: ")
        if bathrooms == "exit": exit()

        sizem2 = input("Size in squared meters: ")
        if sizem2 == "exit": exit()

        print("Area options: " +
              "eixample, ciutat_vella, gracia, horta_guinardo, les_corts," +
              "nou_barris, sant_andreu, sant_marti,sants_montjuic")
        area = input("Area: ")
        if area == "exit": exit()

        price = predictor.predict_prize(int(rooms), int(bathrooms), int(sizem2), area)
        print("Predicted prize: " + str(price))


if __name__ == "__main__":
    main()