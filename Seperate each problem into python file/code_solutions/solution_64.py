import math

def get_lat_long(lat, lon):
    """
    Returns the latitude and longitude of the given latitude and longitude.
    """
    # convert the latitude and longitude to radians
    lat = math.radians(lat)
    lon = math.radians(lon)

    # calculate the distance between the two points
    delta_lat = lat - 37.423021