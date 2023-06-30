def findsum(arr,n):
    first=-9090
    second=-9090
    for i in range(len(arr)):
        if arr[i]>first:
            second=first
            first=arr[i]
        elif arr[i]>second and arr[i]!=first:
            second=first
    return (first+second)
arr = [12, 34, 10, 6, 40]
result=findsum(arr,len(arr))
print(result)