import numpy as np
import csv

def odd_array(ar):
    odd_ar = np.array([], 'int')
    for i in range(len(ar)):
        if (ar[i] % 2 != 0):
            odd_ar = np.append(odd_ar, ar[i], axis=None)
    return odd_ar

def odd_array_index(ar):
    odd_ar = np.array([], 'int')
    for i in range(1, len(ar), 2):
        odd_ar = np.append(odd_ar, ar[i], axis=None)
    return odd_ar



rand_array = np.random.randint(0, 100, 100)
print(rand_array)

for i in range(len(rand_array)-1):
    for j in range(len(rand_array)-i-1):
        if rand_array[j] > rand_array[j+1]:
            m = rand_array[j]
            rand_array[j] = rand_array[j+1]
            rand_array[j+1] = m


np_file = open('np_array.csv', 'w')
with np_file:
    writer = csv.writer(np_file)
    writer.writerow(rand_array)
    writer.writerow(odd_array(rand_array))
    writer.writerow(odd_array_index(rand_array))

print(rand_array)
print(odd_array(rand_array))
print(odd_array_index(rand_array))