def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def mergeSort(n):
    if len(n) > 1:
        mid = len(n) // 2
        left_half = n[:mid]
        right_half = n[mid:]
        mergeSort(left_half)
        mergeSort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                n[k] = left_half[i]
                i += 1
            else:
                n[k] = right_half[j]
                j += 1
            k+=1

        while i < len(left_half):
            n[k] = left_half[i]
            i += 1
            k += 1
        
        while j < len(right_half):
            n[k] = right_half[j]
            j += 1
            k += 1


def quickSort(n):
    quick_sort_helper(n, 0, len(n)-1)

def quick_sort_helper(n, low, high):
    if low < high:
        pi = partition(n, low, high)
        quick_sort_helper(n, low, pi-1)
        quick_sort_helper(n, pi+1, high)

def partition(n, low, high):
    pivot = n[high]
    i = (low-1)
    for j in range(low, high):
        if n[j] < pivot:
            i+=1
            n[i], n[j] = n[j], n[i]
    n[i+1], n[high] = n[high], n[i+1]
    return i + 1

def runFibonacci():
    n = 10
    print("Fibonacci sequence: ")
    for i in range(n):
        print(fibonacci(i), end = " ")
    print()

def runFactorial():
    n = 5
    print(f"Factorial of {n} (recursive): {factorial(n)}")
    print()

def runMerge():
    n = [38, 27, 43, 3, 9, 82, 10]
    mergeSort(n)
    print(f"Sorted array using Merge Sort: {n}")
    print()

def runQuick():
    n = [38, 27, 43, 3, 9, 82, 10]
    quickSort(n)
    print(f"Sorted array using Quick Sort: {n}")
    print()

runFibonacci()
print()
runFactorial()
runMerge()
runQuick()