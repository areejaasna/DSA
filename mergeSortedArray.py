#merge sorted array without using extra space
def mergeSorted(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    left = n-1
    right = 0
    while (left >=0 and right < m):
        if(arr1[left] > arr2[right]):
            arr1[left], arr2[right] = arr2[right], arr1[left]
            left -=1
            right +=1
        else:
            break
    arr1.sort()
    arr2.sort()
    mergedArray = arr1+arr2
    return mergedArray


arr1 = [1, 2, 5, 7]
arr2 = [0, 2, 6, 8, 9]
mArray = mergeSorted(arr1,arr2)

for ele in mArray:
    print(ele, end=" ")
