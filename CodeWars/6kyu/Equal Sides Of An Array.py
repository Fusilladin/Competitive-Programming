def find_even_index(arr):
    print(arr)
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            
            return i
    else:
        return -1
