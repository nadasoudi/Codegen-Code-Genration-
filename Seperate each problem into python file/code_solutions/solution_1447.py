import geopy

# Create a geopy object
geolocator = geopy.geocoders.Nominatim(user_agent="my_app")

# Create a geopy object
location = geolocator.geocode("Mumbai, India")

# Print the location
print(location.address)

# Print the latitude and longitude
print(location.latitude, location.longitude)