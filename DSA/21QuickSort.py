# sorting algorithms
# Quick sort

'''def QuickSort(arr, l , r):  # l-length R-right
    if (l < r):
       p = parition(arr, l ,r)

       QuickSort(arr, l, p-1)
       QuickSort(arr, p+1, r)

def parition(arr, l, r):
    pivot = arr[l]

    i = l+1
    j = r
    while True:
        while (i < j and arr[i] <pivot):
            i = i+1

        while (i < j and arr[i] >pivot):
            j =j-1

        if (i < j):
            arr[i], arr[j]  = arr[j], arr[i]
        else:
            break
               
    arr[l], arr[j] = arr[j], arr[l]      

    return j

a#rr = [23,34,56,76,12,4,56,44]
#QuickSort(arr, 0, len(arr)-1)  
#print(arr)'''

def QuickSort(arr, l, r):
    if l < r:
        p = partition(arr, l, r)
        QuickSort(arr, l, p - 1)
        QuickSort(arr, p + 1, r)

def partition(arr, l, r):
    pivot = arr[r]
    i = l - 1
    for j in range(l, r):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1

arr = [23, 34, 56, 76, 12, 4, 56, 44]
QuickSort(arr, 0, len(arr) - 1)
print(arr)