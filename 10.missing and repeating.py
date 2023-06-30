def fun(arr,n):
    for j in range(1,len(arr)):
        key=arr[j]
        i=j-1
        while(i>=0 and key< arr[i]):
            arr[i+1]=arr[i]
            i=i-1
        arr[i+1]=key
    print(arr)
    for i in range(1,len(arr)):
        if arr[i]-arr[i-1]>1:
            print('missing term is ',arr[i]-1)
        if arr[i]-arr[i-1]==0:
            print('repeating term is ',arr[i])
arr=[4,3,6,2,1,1]
fun(arr,len(arr))


