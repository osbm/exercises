import numpy

# 1'den 1000'e kadar sayıların olduğu bir NumPy array oluşturun ve bu dizide 18 ile tam bölünen sayıları seçen bir sorgu yazın.
a = numpy.arange(1001)
print(a[a % 18 == 0])