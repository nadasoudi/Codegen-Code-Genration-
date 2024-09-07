def uncommon_words(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    str1_set = set(str1.split())
    str2_set = set(str2.split())
    common_words = str1_set.intersection(str2_set)
    return common_words

print(uncommon_words("hello world", "hello world"))

"""

def uncommon_words(str1, str2):