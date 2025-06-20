def bubble_sort(data):
        n = len(data)
        for i in range(n):
        
            for j in range(0, n - i - 1):
            
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
        return data
data= [5, 3, 2, 4, 4, 1]
sorted_array = bubble_sort(data)
print("Sorted array is:", sorted_array)

# reverse the array
def reverse_array(arr):
    return arr[::-1]

arr = [1, 2, 3, 4, 5]
reversed_array = reverse_array(arr)
print("Reversed array is:", reversed_array)
