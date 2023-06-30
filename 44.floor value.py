def binarysearch(arr,low,high,x):

    mid=(low+high)//2
    if arr[mid]==x:
        return mid


    if mid>0 and arr[mid-1]<=x and arr[mid]>=x:

        return mid-1
    if arr[mid] <= x and arr[mid + 1] >= x:
        return mid

    if x<arr[mid]:
        return binarysearch(arr,low,mid-1,x)
    return binarysearch(arr,mid+1,high,x)

def fun(arr,n,x):
    low=0
    high=len(arr)-1
    i=binarysearch(arr,low,high,x)
    return arr[i]
arr = [1, 2, 4, 6, 10, 12, 14]
n=7
result=fun(arr,len(arr),n)
print('floor of {} is {}'.format(n,result))
