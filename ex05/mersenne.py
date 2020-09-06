Python 3.7.7 (default, May  6 2020, 11:45:54) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> mersenne=[2**k-1 for k in range(1, 65)]
>>> a= 31
>>> if a in mersenne:
	print('YES')
else:
	print('NO')

	
YES
>>> a= 2047
>>> if a in mersenne:
	print('YES')
else:
	print('NO')

	
YES
>>> 