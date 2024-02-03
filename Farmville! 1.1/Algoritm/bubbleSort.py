def bubble(list_a):
    indexing_lenght = len(list_a) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, indexing_lenght):
            if list_a[i] > list_a[i+1]:
                list_a[i], list_a[i+1] = list_a[i+1], list_a[i]
                sorted = False

    return list_a
myList = [4, 6, 8, 3, 2, 5, 7, 8, 9]

print(bubble(myList))
