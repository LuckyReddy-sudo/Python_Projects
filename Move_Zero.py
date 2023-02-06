# From a list of numbers,movee zero to the end of the list.

list = [1, 0, 2, 0, 4, 6]

for i in list:
    if i == 0:
        list.remove(i)
        list.append(i)
print(list)