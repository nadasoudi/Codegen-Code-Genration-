import numpy as np

def convert_degrees_to_radians(degrees):
    radians = degrees * np.pi / 180
    return radians

def convert_radians_to_degrees(radians):
    degrees = radians * 180 / np.pi
    return degrees

def main():
    degrees = int(input("Enter the degrees: "))
    radians = convert_degrees_to_radians(