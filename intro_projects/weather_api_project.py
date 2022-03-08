# Write a program that makes a request to the weather API and prints out the weather forecast.

# The program takes in the name of the location from the command line, like this:

# python3 ./get_forecast.py "New York City"
# or
# python3 ./get_forecast.py "11224"
# or
# python3 ./get_forecast.py "Tokyo, Japan"
# or whatever else

# The program should produce the following output:
# ```
# Location: "New York City"
# Latitude: 40.71
# Longitude: -74.01
# Temperature (C): 6.1

# It is a bit chilly in New York City.
# ```

# The last part of the output changes depending on how cold/hot it is. Use the following ranges (temperature in celsius):
# Below 0:
# "It is freezing in {location}!"
# Between 0 and 10:
# "It is somewhat cold in {location}."
# Between 10 and 15:
# "It is a bit chilly in {location}."
# Between 15 and 20:
# "It's getting nice in {location}."
# Between 20 and 30:
# "It's very nice out in {location}."
# 30 and over:
# "It is hot in {location}!"

import requests
import json
import sys

API_KEY = '497364ec561740f5812190752220803'

URL = 'http://api.weatherapi.com/v1/current.json'

if (len(sys.argv) < 2):
    raise Exception("You must provide a location as a program argument. (i.e. python3 weather_api_project.py \"Miami\")")

location = sys.argv[1]
r = requests.get(URL, params={
    'key': API_KEY,
    'q': location
})
# r = requests.get(URL + "?key={}&q={}".format(API_KEY, location))
# print(r.content)

weather_data = json.loads(r.content,)
# # # print(json.dumps(y,indent=4))

if "location" not in weather_data:
    print("Could not find location: {}".format(location))
    exit()

location_name = weather_data["location"]["name"]
lat = weather_data["location"]["lat"]
long = weather_data["location"]["lon"]
temp = weather_data["current"]["temp_c"]


# print("Location: \"{}\"".format(location_name))
# # print("Location: " + "\"" + location_name + "\"")
# print("Latitude: {}".format(lat))
# print("Longitude: {}".format(lat))

# # print("Latitude: " + str(lat))
# # print("Longitude: " + str(y["location"]["lon"]))


# # print("Temperature (C): " + str(y["current"]["temp_c"]))

message = ""
if temp < 0:
    message = "\"" + "It is freezing in " + location_name + "!" + "\""
elif temp <= 9:
    message = "\"" + "It is somewhat cold in " + location_name + "." + "\""
elif temp <= 14:
    message = "\"" + "It is a bit chilly in " + location_name + "." + "\""
elif temp <= 19:
    message = "\"" + "It's getting nice in " + location_name + "." + "\""
elif temp <= 29:
    message = "\"" + "It's very nice in " + location_name + "." + "\""
else:
    message = "\"" + "It is hot in " + location_name + "." + "\""


print("""Location: "{}"
Latitude: {}
Longitude: {}
Temperature (C): {}
{}""".format(location_name, lat, long, temp, message))
