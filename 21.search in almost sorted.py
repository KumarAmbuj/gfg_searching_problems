def binarysearch(arr,low,high,x):

    mid=(low+high)//2
    if arr[mid]==x:
        return mid
    if mid>low and arr[mid-1]==x:
        return  mid-1

    if mid<high and arr[mid+1]==x:
        return mid+1

    if x<arr[mid]:
        return binarysearch(arr,low,mid-2,x)
    return binarysearch(arr,mid+2,high,x)
arr = [3, 2, 10, 4, 40]
result=binarysearch(arr,0,len(arr)-1,4)
print(result)


