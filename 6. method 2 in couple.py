def maxmin(arr,n):
    if n%2==0:
        mx=max(arr[0],arr[1])
        mn=min(arr[0],arr[1])
        i=2
    else:
        ma=mi=arr[0]
        i=1
    while(i<n-1):
        if arr[i]<arr[i+1]:
            mx=max(mx,arr[i+1])
            mn=min(mn,arr[i])
        else:
            mx=max(mx,arr[i])
            mn=min(mn,arr[i+1])
        i=i+2
    return(mx,mn)
arr=[1000,11,445,1,330,3000]
max,min=maxmin(arr,len(arr))
print('max is ',max)
print('min is ',min)

