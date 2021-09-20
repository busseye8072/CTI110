Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 123.4567
123.4567
>>> format(123.45678, '.2f')
'123.46'
>>> x=123.456789
>>> format(x,'10')
'123.456789'
>>> format(x,'15')
'     123.456789'
>>> format(x,'15.2f')
'         123.46'
>>> print("Price for item $",x)
Price for item $ 123.456789
>>> print("Price for item $",x,sep="")
Price for item $123.456789
>>> print("Price for item $",format(x,'.2f'