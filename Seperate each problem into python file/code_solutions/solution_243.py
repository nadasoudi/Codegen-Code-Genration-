def area(r, r1, r2, r3):
    return (r * (r1 + r2 + r3)) / 2

r = float(input("Enter the radius of the sector: "))
r1 = float(input("Enter the radius of the first sector: "))
r2 = float(input("Enter the radius of the second sector: "))
r3 = float(input("Enter the radius of the third sector: "))
print("The area of the sector is: ", area