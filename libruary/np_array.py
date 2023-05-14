import numpy as np

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

def sort_array(ar):
    for i in range(len(ar) - 1):
        for j in range(len(ar) - i - 1):
            if ar[j] > ar[j + 1]:
                m = ar[j]
                ar[j] = ar[j + 1]
                ar[j + 1] = m
    return ar