def find_target(arr, target):
    pos = []
    for i in range(len(arr)-1):
        if arr[i] == target:
            pos.append(i)
            
    return pos
arr = [1,2,5,2,3]
target = 2
arr.sort()

print(find_target(arr, target))

