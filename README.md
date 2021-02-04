# Barcelona Renting Price Predictor

_A predictor of renting prices in Barcelona._

## How to try it 🚀

### Requirements 📋

```
python3
```

### Using 🔧

Download the files and execute main.py. The program will ask for the data of the apartment you want to predict the price of.

First it will ask for rooms, then bathrooms and then the size in squared meters. Answer to these with integers. Finally it will ask for the district where the apartment is, and it will show a list of possibilities. Select one by typing it into the field exactly as it is shown. The program will then predict the price and show it on screen.

```
Rooms: 2
Bathrooms: 1
Size in squared meters: 60
Area options: eixample, ciutat_vella, gracia, horta_guinardo, les_corts, nou_barris, sant_andreu, sant_marti,sants_montjuic, sarria_sant_gervasi
Area: ciutat_vella
Predicted price: 938.69€
```

To stop the program just type 'exit' at any point.

```
Rooms: exit
```

## Process

The idea of this small project was to put in practice some theory I learned through an online course. The focus was to build a multilinear regression model that used the gradient descent algorithm to predict the renting prices of apartments in Barcelona.

The first step was to gather apartments data (Price, Rooms, Bathrooms, Size in m2 and District), so I used [Web Scraper](https://webscraper.io/) to scrape over 15,000 apartments on the city.

Then I cleaned the data deleting incomplete entries, duplicates and outliers. In order to do that I created the file data_cleaner.py. All of this process can be found on the data_cleaning folder.

Once I had clean data to work with, I implemented a lineal regression model that used the gradient descent algorithm to find a vector that would be used to predict prices. To make the algorithm faster and more accurate I normalized the values of the size in m2, the rooms and the bathrooms. To check that the results obtained were correct, I also implemented a normal equation calculator that works better in this case since the data gathered is not massive.

Finally I created a class called PricePrediction that handles all the operations to predict the renting prices, and then implemented a quick main.py file that could be used to test the accuracy of the model.

Attempt | #1 | #2 | #3 | #4 | #5 | #6 | #7 | #8 | #9 | #10 | #11
--- | --- | --- | --- |--- |--- |--- |--- |--- |--- |--- |---
Seconds | 301 | 283 | 290 | 286 | 289 | 285 | 287 | 287 | 272 | 276 | 269

## Tools used 🛠️

* [Python](https://www.python.org/) - Language used
* [Web Scraper](https://webscraper.io/) - To scrape the apartments data
* [NumPy](https://numpy.org/) - For the mathematic operations

## Version 📌

1.0

## Authors ✒️

* **Alex Ayza** - *Keys presser* - [aayzaa](https://github.com/aayzaa)

## Licence 📄

Use any of the code however you want!

---
⌨️ with ❤️ by [aayzaa](https://github.com/aayzaa)
