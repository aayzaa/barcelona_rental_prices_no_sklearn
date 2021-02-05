# 📈 Barcelona Rental Price Predictor 📉

_A predictor of rental prices of apartments in Barcelona._

## How to try it 💻

### Requirements

```
python3
numpy
```

### Use

Download the files and execute main.py. The program will ask for the data of the apartment you want to predict the price of.

First it will ask for rooms, then bathrooms and then the size in squared meters. Answer these with integers. Finally it will ask for the district where the apartment is, and it will show a list of possibilities. Select one by typing it into the field exactly as it is shown. The program will then predict the price and show it on screen.

```
Rooms: 2
Bathrooms: 1
Size in squared meters: 60
Area options: eixample, ciutat_vella, gracia, horta_guinardo, les_corts, nou_barris, sant_andreu, sant_marti,sants_montjuic, sarria_sant_gervasi
Area: ciutat_vella
Predicted price: 938.69€
```

To stop the program just type `exit` at any point.

```
Rooms: exit
```

## Process 👩🏽‍💻

The idea of this small project was to put in practice some theory I learned through an online course. The focus was to build a multilinear regression model that used the gradient descent algorithm to predict the rental prices of apartments in Barcelona.

The first step was to gather data on apartments (Price, Rooms, Bathrooms, Size in m2 and District), so I used [Web Scraper](https://webscraper.io/) to **scrape over 15,000 apartments** in the city.

Then I **cleaned the data** deleting incomplete entries, duplicates and outliers. In order to do that I created the file data_cleaner.py. All of this process can be found in the data_cleaning folder.

Once I had clean data to work with, I **implemented a linear regression model that used the gradient descent algorithm** to find a vector that would be used to predict prices. To make the algorithm faster and more accurate I **normalized the values** of the size in m2, the rooms and the bathrooms. To check that the results obtained were correct, I also implemented a normal equation calculator that works better in this case since the data gathered is not massive.

Finally I created a class called **PricePrediction that handles all the operations to predict the rental prices**, and then implemented a quick main.py file that could be used to test the accuracy of the model.

## Results 📊

_Note: this is just a small personal project, so the results of this should be taken with a handful of salt._

I ran some tests to calculate the average error in euros that the model has. The total error average is 353€, since the data includes apartments that cost thousands and thousands of euros. Below there is a table that has the **error depending on the maximum price** taken into account:

Maximum price | 1000€ | 1500€ | 2000€ | 4000€ | All apartments
--- | --- | --- | --- |--- |---
Average error | 76€ | 170€ | 218€ | 295€ | 353€

_For example, for apartments between 0€ and 1500€, the average error is 170€_

After reading the data on 15,000 apartments, the program also defined which neighborhoods are more expensive than others. To my surprise, Eixample and Sant Marti get the two top spots as the most expensive areas on top of Sarria-Sant Gervasi or Ciutat Vella. The **districts ranked from most expensive to least** can be seen below:

| Rank | District |
| --------------- | --------------- |
| 1 | Eixample |
| 2 | Sant Marti |
| 3 | Sarria-Sant Gervasi |
| 4 | Horta-Guinardo |
| 5 | Ciutat Vella |
| 6 | Les Corts |
| 7 | Sants-Montjuic |
| 8 | Sant Andreu |
| 9 | Gracia |
| 10 | Nou Barris |

I also found surprising that having more rooms subtracts from the price of an apartment. You can see the test below, **adding rooms to an apartment decreases the price** of it, while **adding bathrooms increases it** (who doesn't want to have 6 different showers?!!).

```
Rooms: 2
Bathrooms: 1
Size in squared meters: 70
Area options: eixample, ciutat_vella, gracia, horta_guinardo, les_corts, nou_barris, sant_andreu, sant_marti,sants_montjuic, sarria_sant_gervasi
Area: gracia
Predicted price: 915.27€
```
_2 Rooms added._
```
Rooms: 4
Bathrooms: 1
Size in squared meters: 70
Area options: eixample, ciutat_vella, gracia, horta_guinardo, les_corts, nou_barris, sant_andreu, sant_marti,sants_montjuic, sarria_sant_gervasi
Area: gracia
Predicted price: 569.8€
```
_Now, let's add 2 Bathrooms._
```
Rooms: 4
Bathrooms: 3
Size in squared meters: 70
Area options: eixample, ciutat_vella, gracia, horta_guinardo, les_corts, nou_barris, sant_andreu, sant_marti,sants_montjuic, sarria_sant_gervasi
Area: gracia
Predicted price: 1041.13€
```

## Tools used 🛠️

* [Python](https://www.python.org/) - Language used
* [Web Scraper](https://webscraper.io/) - To scrape the apartments data
* [NumPy](https://numpy.org/) - For the mathematic operations

## Version 📌

1.0

## Authors ✒️

* **Alex Ayza** - *Keys presser* - [aayzaa](https://github.com/aayzaa)

## License 📄

Use any of the code however you want!

---
⌨️ with ❤️ by [aayzaa](https://github.com/aayzaa)
