def binary_search_recursice(list, x, low, high):
    size = len(list)
    if low <= high:
        mid = (low+high)//2
        if (list[mid] == x):
            print("element found at", mid+1)
            return True
        elif (list[mid] > x):
            return binary_search_recursice(list, x, low, mid-1)
        elif (list[mid] < x):
            return binary_search_recursice(list, x, mid+1, high)
    else:
        return False


list = [3, 6, 8, 24, 56, 60, 78, 90, 98, 99, 110]
Result = binary_search_recursice(list, 110, 0, len(list)-1)
if Result:
    Result
else:
    print("not found")
