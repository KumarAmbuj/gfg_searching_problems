def binarysearch(arr,low,high):

    mid=(low+high)//2
    if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
        return arr[mid]

    if arr[mid]<arr[mid-1] and arr[mid]>arr[mid+1]:
        return binarysearch(arr,low,mid-1)
    if arr[mid]>arr[mid-1] and arr[mid]<arr[mid+1]:
        return binarysearch(arr,mid+1,high)
arr = [1, 3, 50, 10, 9, 7, 6]
result=binarysearch(arr,0,len(arr)-1)
print(result)