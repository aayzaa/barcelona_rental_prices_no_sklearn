import pandas
import numpy

# Open file with the raw data
data = pandas.read_csv('raw_data/enalquiler-apartamentos-min1hab.csv')

# Clean the price field and turn it into an integer
data['price'] = data['price'].str.replace('\D', '', regex=True).astype(int)

# Clean the rooms and bathrooms fields and turn them into integers
data['rooms'] = data['rooms'].str.replace('\D', '', regex=True).astype(int)
data['bathrooms'] = data['bathrooms'].str.replace('\D', '', regex=True).astype(int)

# Clean the size data and turn it into integers
data['sizem2'] = data['sizem2'].str.replace('m2', '').astype(int)

# The zones where the flats are located is a nominal value, so it needs to be categorized
# In order to do that in a lineal regression model, we use dummy variables
# A dummy variable like 'eixample' will be 1 if the zone is Eixample, and 0 if it's not
# Only one dummy variable can be 1 for each flat (it would need to be really big to be on both!)
# Sarria/SantGervasi is left out as our reference category
# The absence of any 1 in the dummy variables means that the flat is in the reference category
# That is done for performances issues
data['eixample'] = numpy.where(data['zone'].str.contains('Eixample'), 1, 0)
data['ciutat_vella'] = numpy.where(data['zone'].str.contains('Ciutat Vella'), 1, 0)
data['gracia'] = numpy.where(data['zone'].str.contains('Gràcia'), 1, 0)
data['horta_guinardo'] = numpy.where(data['zone'].str.contains('Horta-Guinardó'), 1, 0)
data['les_corts'] = numpy.where(data['zone'].str.contains('Les Corts'), 1, 0)
data['nou_barris'] = numpy.where(data['zone'].str.contains('Nou Barris'), 1, 0)
data['sant_andreu'] = numpy.where(data['zone'].str.contains('Sant Andreu'), 1, 0)
data['sant_marti'] = numpy.where(data['zone'].str.contains('Sant Martí'), 1, 0)
data['sants_montjuic'] = numpy.where(data['zone'].str.contains('Sants / Monjuïc'), 1, 0)

# Delete the undesired columns
to_drop = ["web-scraper-order", "web-scraper-start-url", "zone"]
data.drop(columns=to_drop, inplace=True, axis=1)

# Export the cleaned data
data.to_csv('cleaned_data/barcelona_apartments.csv', index = False)
