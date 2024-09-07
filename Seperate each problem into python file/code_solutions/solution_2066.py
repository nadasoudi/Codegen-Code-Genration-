def mirror_image(image):
    mirror_image = ""
    for i in range(len(image)):
        for j in range(len(image[i])):
            mirror_image += image[i][j]
    return mirror_image

# driver code
image = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(mirror_image(image))

# This code is contributed by Nikhil