def binarysearch(arr,low,high):

    mid=(low+high)//2
    if arr[mid]==mid:
        return mid

    if mid>arr[mid]:
        return binarysearch(arr,mid+1,high)
    else:
        return binarysearch(arr,low,mid-1)
arr = [-10, -1, 0, 3, 10, 11, 30, 50, 100]
result=binarysearch(arr,0,len(arr))
print(result)