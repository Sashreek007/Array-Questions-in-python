import array

arr1 = array.array('i', [2, 4, 3, 5, 6, -2, 4, 7, 8, 9])

def pair_sum(arr, target):
    arr2 = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target and f"{arr[i]}+{arr[j]}" not in arr2:
                arr2.append(f"{arr[i]}+{arr[j]}")
    return arr2

result = pair_sum(arr1, 7)
print(result)