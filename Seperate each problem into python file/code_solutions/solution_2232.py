def remove_duplicates(str):
    # Write your code here
    str = str.replace(" ", "")
    str = str.replace("(", "")
    str = str.replace(")", "")
    str = str.replace("[", "")
    str = str.replace("]", "")
    str = str.replace("{", "")
    str = str.replace("}", "")
    str = str.replace("<", "")
    str = str.replace