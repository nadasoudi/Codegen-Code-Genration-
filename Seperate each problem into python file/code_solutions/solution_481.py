>>> from collections import Counter
>>> from itertools import groupby
>>>
>>> def group_keys(iterable):
...     return groupby(iterable, key=lambda x: x[0])
>>>
>>> def group_values(iterable):
...     return groupby(iterable, key=lambda x: x[1])
>>>
>>> def group_values_by_key(iterable):
...     return groupby(iterable, key=lambda x: x