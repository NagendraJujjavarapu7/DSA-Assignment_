# Example 1:

def array(arr, n):
    n = n % len(arr)
    return arr[-n:] + arr[:-n]
arr = [3, 1, 2, 5, 7]
rotated_array = array(arr, 2)
print(rotated_array)

# Example 2:

def array(arr, n):
    n = n % len(arr)
    return arr[-n:] + arr[:-n]
arr = [1, 2, 3, 4, 5]
rotated_array = array(arr, 1)
print(rotated_array)