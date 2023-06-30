# finding the index of maximum term in rotated sorted array
def findmin(arr,n):

    if len(arr)==1:
        return arr[0]

    if arr[0]<arr[len(arr)-1]:
        return arr[0]
    low=0
    high=len(arr)-1
    index=binarysearch(arr,low,high)

    #index element  is max in array
    #index+1 term is min in sorted rotated array
    return arr[index+1]

def binarysearch(arr,low,high):


    mid=(low+high)//2
    if mid<high and arr[mid]>arr[mid+1]:
        return mid
    if low<mid and arr[mid]<arr[mid-1]:
        return mid-1
    if arr[low]>arr[mid]:
        return binarysearch(arr,low,mid-1)
    return binarysearch(arr,mid+1,high)



arr2 = [2, 3, 4, 5, 6, 7, 8, 1]
result=findmin(arr2,len(arr2))
print(result)