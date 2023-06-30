# finding no of count using binary search
def binarysearch(arr,low,high):
    mid=(low+high)//2
    if (mid==high or arr[mid+1]==0) and arr[mid]==1:
        return mid+1

    if arr[mid]==1:
        return binarysearch(arr,mid+1,high)
    return binarysearch(arr,low,mid-1)
def noofcount(arr,n):
    low=0
    high=n-1
    x=binarysearch(arr,low,high)
    return x
arr=[1, 1, 1, 0, 0, 0,0]
count=noofcount(arr,len(arr))
print(count)
