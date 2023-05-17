import numpy as np
import csv
from libruary import np_array
from classes import Horse, Dog, Cat

rand_array = np.random.randint(0, 100, 100)
print(rand_array)

rand_array = np_array.sort_array(rand_array)

np_file = open('output_file/np_array.csv', 'w')
with np_file:
    writer = csv.writer(np_file)
    writer.writerow(rand_array)
    writer.writerow(np_array.odd_array(rand_array))
    writer.writerow(np_array.odd_array_index(rand_array))

print(rand_array)                               # Формирование массива
print(np_array.odd_array(rand_array))           # Выбор нечётных элементов
print(np_array.odd_array_index(rand_array))     # Выбор элементов по нечётным индексам


# Classes Animals

horse_betty = Horse("Betty", "Perissodactyla", "racehorse")
print(type(horse_betty), horse_betty.name, horse_betty.sound)
dog_dagger = Dog(  "Dagger", "Caninae", "Champion of the country")
print(type(dog_dagger), dog_dagger.name, dog_dagger.sound)
cat_kitty = Cat("Kitty", "Feline", "KittyCat")
print(type(cat_kitty), cat_kitty.name, cat_kitty.sound)