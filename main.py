import numpy as np
import csv
from libruary import np_array

rand_array = np.random.randint(0, 100, 100)
print(rand_array)

rand_array = np_array.sort_array(rand_array)


np_file = open('output_file/np_array.csv', 'w')
with np_file:
    writer = csv.writer(np_file)
    writer.writerow(rand_array)
    writer.writerow(np_array.odd_array(rand_array))
    writer.writerow(np_array.odd_array_index(rand_array))

print(rand_array)
print(np_array.odd_array(rand_array))
print(np_array.odd_array_index(rand_array))