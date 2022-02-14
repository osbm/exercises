import numpy

a = numpy.arange(50)
numpy.random.shuffle(a)

def func(array):
    sorted_array = numpy.array([])
    while array.size > 0:
        index = array.argmin()
        sorted_array = numpy.append(sorted_array, array[index])
        array = numpy.delete(array, index)
        
    return sorted_array

print(func(a))
