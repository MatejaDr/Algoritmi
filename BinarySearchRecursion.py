def binary_search(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if data[mid] == target:
            return True
        elif data[mid] > target:
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid+1, high)
        
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7  
low = 0  
high = len(data) - 1  

result = binary_search(data, target, low, high)

if result:
    print(f"Found {target} in the list!")
else:
    print(f"{target} not found in the list.")

