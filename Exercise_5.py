# Time Complexity:
# Best Case: O(n log n) - When the pivot divides the array into two equal halves.
# Worst Case: O(n^2) - When the pivot is always the smallest or largest element.
# Average Case: O(n log n) - When the partitions are reasonably balanced.

# Space Complexity:
# O(log n) in the best case (balanced partitions).
# O(n) in the worst case (unbalanced partitions).
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No

# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
    i = l - 1  
    pivot = arr[h] 
    for j in range(l, h):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return i + 1


def quickSortIterative(arr, l, h):
    size = h - l + 1
    stack = [0] * size
    top = -1
    top += 1
    stack[top] = l
    top += 1
    stack[top] = h
    while top >= 0:
        h = stack[top]
        top -= 1
        l = stack[top]
        top -= 1
        p = partition(arr, l, h)
        if p - 1 > l:
            top += 1
            stack[top] = l
            top += 1
            stack[top] = p - 1
        if p + 1 < h:
            top += 1
            stack[top] = p + 1
            top += 1
            stack[top] = h
            
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr)
quickSortIterative(arr, 0, n - 1)
for i in range(n):
  print(arr[i], end=" ")