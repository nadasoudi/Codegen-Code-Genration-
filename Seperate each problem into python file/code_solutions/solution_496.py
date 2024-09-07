>>> import decimal
>>> print(decimal.Decimal(1.1))
1.1
>>> print(decimal.Decimal(1.1).as_integer_ratio())
(1, 1)
>>> print(decimal.Decimal(1.1).as_integer_ratio().limit_denominator(1000))
(1, 1)
>>> print(decimal.Decimal(1.1).as_integer_ratio().limit_denominator