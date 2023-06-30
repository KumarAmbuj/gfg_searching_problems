def binarysearch(arr,low,high,x):

    mid=(low+high)//2

    if arr[mid]<=x and arr[mid+1]>=x:
        return mid

    if x<arr[mid]:
        return binarysearch(arr,low,mid-1,x)
    return binarysearch(arr,mid+1,high,x)



def findkclosest(arr,n,k,x):

    low=0
    high=len(arr)-1

    l=binarysearch(arr,low,high,x)
    r=l+1
    count=0
    while(l>=0 and r<n and count<k ):
        if x-arr[l]< arr[r]-x:
            print(arr[l],end=' ')
            l=l-1
        else:
            print(arr[r],end=' ')
            r=r+1
        count+=1


arr = [12, 16, 22, 30, 35, 39, 42,
       45, 48, 50, 53, 55, 56]
findkclosest(arr,len(arr),4,36)