# greedy algorithms

def Max_min_diff(arr):
    arr.sort()
    n = len(arr)
    mid = n//2
    max = 0
    min = 0
    j = n-1

    for i in range(mid):
        max = max + abs(arr[i]- arr[j])
        j = j-1

        min = min + abs(arr[2*i]- arr[2*i+1])
    print("maximun differece", max)
    print("minimun differece", min)

arr=[12,5,25,10,2,15,8,30]
Max_min_diff(arr)