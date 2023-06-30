def sortedrotate(arr,n,x):
    pivot=findpivot(arr,0,n-1)
    print(pivot)

    if list[pivot]==x:
        return pivot

    if list[0]<=x:
        return binarysearch(arr,0,pivot-1,x)
    return binarysearch(arr,pivot+1,n-1,x)

def findpivot(arr,low,high):

    if high<low:
        return -1
    if high==low:
        return low

    mid=int((low+high)/2)

    if mid<high and arr[mid]>arr[mid+1]:
        return mid

    if low<mid and arr[mid]<arr[mid-1]:
        return (mid-1)

    if arr[low]>=arr[mid]:
        return findpivot(arr,low,mid-1)
    return findpivot(arr,mid+1,high)

def binarysearch(arr,low,high,key):

    if low<high:
        mid = int((low + high) / 2)

        if arr[mid]==key:
            return mid

        if key<arr[mid]:
            return binarysearch(arr,low,mid-1,key)

        elif key>arr[mid]:
            return binarysearch(arr,low+1,high,key)

list=[5, 6, 7, 8, 9, 10, 1, 2, 3]
n=len(list)
p=sortedrotate(list,n,3)
print(p)



