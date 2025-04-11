def bubble_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        for j in range(0, n-i-1):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]= lst[j+1],lst[j]
    return lst

numbers = [5,3,8,4,2]
bubble_sort(numbers)
print(numbers)

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i] # i = 1 lst[1] = 3
        j = i - 1   # j = 0
        while j >= 0 and key < lst[j]: # 3 < 5
            lst[j + 1] = lst[j] # lst[1] = lst[0]
            j -= 1  # j = -1
        lst[j + 1] = key # lst[0] = 3
    return lst

numbers = [5,3,8,4,2]
insertion_sort(numbers)
print(numbers)

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1,n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

numbers = [5,3,8,4,2]
selection_sort(numbers)
print(numbers)

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

print(quicksort([5, 3, 8, 4, 2]))
# Виведе: [2, 3, 4, 5, 8]

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        return merge(merge_sort(left), merge_sort(right))
    
def merge(left, right):
    merged = []
    left_idx = 0
    right_idx = 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1
    merged.extend(left[left_idx:])
    merged.extend(right[right_idx:])
    return merged