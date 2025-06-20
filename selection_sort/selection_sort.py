def selection_sort(arr):
    data = arr.copy() 
    n = len(data)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if data[j] < data[min_index]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]
    return data
arr = [4, 3, 5, 1, 2]
sorted_array = selection_sort(arr)
print("Sorted array is:", sorted_array)

# reverse the array
def reverse_array(arr):
    return arr[::-1]

arr = [1, 2, 3, 4, 5]
reversed_array = reverse_array(arr)
print("Reversed array is:", reversed_array)