def split_array(array, x):
    subarrays = []
    current_subarray = []
    current_sum = 0
    for num in array:
        current_subarray.append(num)
        current_sum += num
        if current_sum > x:
            subarrays.append(current_subarray[:-1])
            current_subarray = [num]
            current_sum = num
    subarrays.append(current_subarray)
    return subarrays


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = 15
result = split_array(array, x)
print(result)