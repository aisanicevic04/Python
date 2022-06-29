def binary_search(array):
    item = int(input("unesite neki broj: "))
    array.sort()
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if array[mid] == item:
            return array[item]
        elif item < array[mid]:
            end = mid - 1
        else:
            start = mid + 1


print(binary_search(list(range(0, 11))))
