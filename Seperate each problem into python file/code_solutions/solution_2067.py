import re

text = "The rain in Spain"
pattern = r"\b\w+\.\w+"

# Substituting pattern in text
# text = re.sub(pattern, r"\1*******", text)

# Substituting pattern in text
text = re.sub(pattern, r"\1*******", text)

# Printing the modified text
print(text)

# Python program to find all matches
# in a string

# Function to find all