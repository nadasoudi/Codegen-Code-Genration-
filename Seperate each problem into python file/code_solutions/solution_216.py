import geopy.geocoders
from geopy.geocoders import Nominatim

# Enter the state name:
state = input("Enter the state name: ")

# Enter the country name:
country = input("Enter the country name: ")

# Create a geolocator object:
geolocator = Nominatim(user_agent="myGeoPy")

# Create a geocoder object: