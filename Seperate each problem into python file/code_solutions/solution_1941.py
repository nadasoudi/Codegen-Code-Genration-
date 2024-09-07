import re

def solution(s):
    s = re.sub(r'\s+','', s)
    s = s.lower()
    s = s.split()
    s = [x for x in s if x not in set(string.punctuation)]
    s =''.join(s)
    s = s.split()
    s = [x for x in s if x not in set(string.punctuation)]
    s =''.join(s)