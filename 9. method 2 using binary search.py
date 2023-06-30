def binarysearch(arr,low,high,x):
    mid=(low+high)//2

    if arr[mid]==x:
        return mid
    if x<arr[mid]:
        return binarysearch(arr,low,mid-1,x)
    return binarysearch(arr,mid+1,high,x)

def findnoofcount(arr,x):
    low=0
    high=len(arr)
    index=binarysearch(arr,low,high,x)

    left=index-1
    count=1
    while(index>0 and arr[left]==x):
        count+=1
        left-=1


    right=index+1
    while(right<high and arr[right]==x):
        count+=1
        right=right+1

    return count
arr=[1,2,2,2,2,3,4,7,8,8]
result=findnoofcount(arr,2)
print(result)