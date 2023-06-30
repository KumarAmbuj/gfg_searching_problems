#find index of max element in array using binary search
def binarysearch(arr,low,high):
    mid=(low+high)//2
    if mid<high and arr[mid]>arr[mid+1]:
        return mid
    if low<mid and arr[mid]<arr[mid-1]:
        return mid-1

    if arr[low]>arr[mid]:
        return binarysearch(arr,low,mid-1)
    return binarysearch(arr,mid+1,high)

def findsum(arr,sum):
    n=len(arr)
    low=0
    high=len(arr)-1
    i=binarysearch(arr,low,high)
    print(i)
    l=(i+1)%n
    r=i
    resl=0
    resr=0

    while(l!=r):
        if (arr[l]+arr[r])==sum:
            resl=l
            resr=r
            break
        if (arr[l]+arr[r])<sum:
            l=(l+1)%n
        else:
            r=(n+r-1)%n
    else:
        print('sum not found ')
        return
    print('sum found no is {} and {} '.format(arr[resl],arr[resr]))
arr = [11, 15, 6, 7, 9, 10]
findsum(arr,26)


