def quickSearch(arr, high, low):
    size = len(arr)
    if size > 1:
        pivot = arr[high]
        right_elements = []
        left_elements = []
        for i in range(size):
            left = 0
            right = 0
            if arr[i] > pivot:
                right_elements.append(arr[i])
                right += 1
            elif arr[i] < pivot:
                left_elements.append(arr[i])
                left += 1

    else:
        return arr
    return quickSearch(left_elements, left, low) + [pivot] + quickSearch(right_elements, right, low)


list = [54, 65, 35, 89, 23, 74, 4, 98, 24]
result = quickSearch(list, len(list)-1, 0)
print(result)
