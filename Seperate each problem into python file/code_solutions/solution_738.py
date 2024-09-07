import geopy.geocoders
import geopy.distance

# Geolocation API
geolocator = geopy.geocoders.Nominatim(user_agent="myGeoLocation")

# Geocode the location
location = geolocator.geocode(input("Enter the location: "))

# Print the latitude and longitude
print(location.latitude, location.longitude)