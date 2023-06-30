def binarysearch(arr,low,high,x):
    mid=(low+high)//2
    if high>=low:
        if arr[mid] == x:
            return mid

        if x < arr[mid]:
            return binarysearch(arr, low, mid - 1, x)
        return binarysearch(arr, mid + 1, high, x)


def findindex(arr,n,key):
    l=0
    h=1
    val=0
    while(val<key):
        l=h
        h=2*h
        val=arr[h]
    index=binarysearch(arr,l,h,key)
    print(index)
arr = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170]
findindex(arr,len(arr),10)