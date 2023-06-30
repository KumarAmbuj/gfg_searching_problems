def maxmin(arr,n):
    max=arr[0]
    min=arr[0]
    for i in range(1,n):
        if arr[i]>max:
            max=arr[i]
        elif arr[i]<min:
            min=arr[i]
    print('max is ',max)
    print('min is ',min)
arr=[1000,11,445,1,330,3000]
maxmin(arr,len(arr))


