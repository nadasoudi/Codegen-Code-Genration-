>>> import re
>>> string = "1,2,3.4,5.6,7.8,9.9,10.10"
>>> string = re.sub(',', '.', string)
>>> string = re.sub('.', ',', string)
>>> string = re.sub('\.', '.', string)
>>> string = re.sub('\,', '.', string)
>>> string = re.sub('\.', '.', string)
>>> string = re