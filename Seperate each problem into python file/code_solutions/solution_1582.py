def anagram(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    s1 = s1.replace(' ', '')
    s2 = s2.replace(' ', '')
    s1 = s1.replace('-', '')
    s2 = s2.replace('-', '')
    s1 = s1.