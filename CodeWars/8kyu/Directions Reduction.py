opposite = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}
def dirReduc(arr):
    print(arr)
    i = 0
    while i < (len(arr)-1):
        current = arr[i]
        _next = arr[i+1]
        if _next == opposite[current]:
            arr.pop(i)
            arr.pop(i)
            i = 0
        else:
            i+=1
    return arr