def first_last_colors(colors):
    if len(colors) == 0:
        return "No colors"
    elif len(colors) == 1:
        return colors[0]
    else:
        return colors[0] + " and " + colors[-1]

print(first_last_colors(["Red", "Green", "Blue", "Black"]))

"""

def first_last_colors(colors):