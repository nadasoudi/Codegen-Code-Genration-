def add_ing_ly(str):
    if len(str) < 3:
        return str + 'ly'
    else:
        return str + 'ing'

print(add_ing_ly('sims'))
print(add_ing_ly('welcome'))
print(