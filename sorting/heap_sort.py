def heapify(arr, size, index, is_min_heap):
    swap_index = index
    left_index = index*2+1
    right_index = index*2+2
    if left_index < size:
        if ((not is_min_heap) and arr[swap_index] < arr[left_index]) or (is_min_heap and arr[swap_index] > arr[left_index]):
            swap_index = left_index

    if right_index < size:
        if ((not is_min_heap) and arr[swap_index] < arr[right_index]) or (is_min_heap and arr[swap_index] > arr[right_index]):
            swap_index = right_index

    if swap_index != index:
        temp = arr[swap_index]
        arr[swap_index] = arr[index]
        arr[index] = temp
        heapify(arr, size, swap_index, is_min_heap)


def sort(arr, is_desc=False):
    size = len(arr)
    for i in range(size//2-1, -1, -1):
        heapify(arr, size, i, is_desc)

    for i in range(size-1, -1, -1):
        temp = arr[0]
        arr[0] = arr[i]
        arr[i] = temp
        heapify(arr, i, 0, is_desc)


my_arr = [4, 5, 7, 1, -2, 1]
sort(my_arr, True)
print(my_arr)




