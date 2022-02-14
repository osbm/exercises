import numpy

# Bir numpy dizisindeki en büyük 3 elemanı seçecek tek satırlık bir kod yazın.

a = numpy.arange(17)



print(numpy.sort(a)[-3:])


# this looks like im cheatin but if this would be a random data set, iwould just sort it by numpy.sort(a)    :)