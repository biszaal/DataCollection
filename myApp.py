import requests, geopandas, geopy, csv, pandas as pd, pathlib, json, re
from pathlib import Path
from bs4 import BeautifulSoup


### GLOBAL VARIABLES ######
double_lng = 0
double_lat = 0
int_tempreture = 0
str_population = 0
bool_file_empty = False
str_city_name = None
str_country_name = None
arr_cities = []
###########################

'''
This method will get the location and using open weather's API it will set the int_tempreture
'''
def setWeather(str_location):
    str_API = '3f5a0660a8fe70340eaa464fa05237cb'
    float_version = 2.5

    file = 'http://api.openweathermap.org/data/' + str(
        float_version) + '/weather?q=' + str_location + '&units=imperial&APPID=' + str_API

    webpage = requests.get(file)
    code = webpage.json()
    global int_tempreture
    if 'main' in code.keys():
        int_tempreture = fehToCel(code['main']['temp'])
    else:
        int_tempreture = 0

'''
This is just converting Fahrenheit to Celsius
'''
def fehToCel(int_Feh):
    int_cel = (int_Feh - 32) * (5 / 9)
    return int(int_cel)

'''
This method will use Google Maps API and this will get the name of any location and set double_lng(longitude) and double_lat(latitude)
'''
def setLonLat(str_argLocation):
    global str_country_name

    str_API = 'AIzaSyAtgV4jqBsFYjCP_peAA2sE3aIIZIOlJ44'
    str_argLocation = str_argLocation.replace(' ', '+')       #replacing space ' ' with plus '+' for it to work with html
    file = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + str_country_name+ ',' + str_argLocation + '&key=' + str_API

    webpage = requests.get(file)

    code = webpage.json()

    global double_lat
    global double_lng
    double_lat = code["results"][0]["geometry"]["location"]["lat"]
    double_lng = code["results"][0]["geometry"]["location"]["lng"]

'''
This part of the method just gathers all the information of a city in the country and arrange it and save it in the csv file
'''
def implement_city_info():
    global bool_file_empty
    global str_population
    global int_tempreture


    Path(str_country_name + '.csv').touch()
    f_read = open(str_country_name + '.csv', 'r')
    # if the file is empty this will let you know and make new file with (name of the country).csv
    if f_read.read():
        bool_file_empty = False
    else:
        bool_file_empty = True
    f_read.close()

    # implementation starts
    f_write = open(str_country_name + '.csv', 'a+')
    if bool_file_empty:
        f_write.write('Name, Population, Longitude, Latitude, Tempreture\n')

    ## The API i am using (Open_Weather) does not support all cities so for that below's code will print not supported
    if (int_tempreture == 0):
        int_tempreture = "N/A"
    else:
        int_tempreture = str(int_tempreture)
    ################

    f_write.write(str_city_name + ", " + str(str_population).replace("," , "") + ", " + str(double_lng) + ", " + str(double_lat) + ", " +
        int_tempreture + "°C" + "\n")
    f_write.close()


'''
Below two methods are not using API but I am pulling information from the following website to get name of the cities of 
any country using and also getting population beautiful soup. This also include some html informations and using 
regular expressions to find any specific letters. 
For example, soup.find("table") will go to the html code of that website and find and print the first table it has.
Why Table? Because in that website the name of cities and its population in stored in a table.
'''
def set_city_population():
    global str_population
    global str_city_name

    file = 'http://worldpopulationreview.com/world-cities'
    webpage = requests.get(file).text
    soup = BeautifulSoup(webpage, "html.parser")

    tableTag = soup.find("table")
    tableData = []
    tableRows = tableTag.find_all('tr')

    for row in tableRows:
        tableCol = row.find_all('td')

        listData = []

        for col in tableCol:
            listData.append(col.text.strip())

        tableData.append(listData)

    for i in range(1,len(tableData)):
        if (str_city_name == tableData[i][1]):
            str_population = str(tableData[i][2])
    if (str_population == None):
        print("Please enter correct name.")

def get_city_names():
    global str_country_name
    global arr_cities

    file = requests.get("http://worldpopulationreview.com/countries/" + str_country_name.lower() + "-population/cities/").text
    soup = BeautifulSoup(file, "html.parser")

    tableData = []

    tableRows = soup.find_all('tr')
    for row in tableRows:
        tableCol = row.find_all('td')
        listData = []

        for col in tableCol:
            listData.append(col.text.strip())

        tableData.append(listData)

    for i in range(1, len(tableData)):
        arr_cities.append(tableData[i][0])


'''
This is the main method
'''
str_country_name = input('Please enter the Country\'s Name: ')
get_city_names()

for str_city_name in arr_cities:
    setLonLat(str_city_name)
    setWeather(str_city_name)
    set_city_population()
    implement_city_info()

print("Source of Population is \"http://worldpopulationreview.com/countries/"+ str_country_name + "-population/\"")
print("Source of Weather is https://openweathermap.org API")
print("Source of Location is https://googlemaps.com API")
