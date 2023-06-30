def fun(arr,n):
    first=second=arr[0]
    for i in range(1,n):
        if arr[i]<first:
            second=first
            first=arr[i]
        elif arr[i]< second and arr[i]!=first:
            second=arr[i]
    print('min is',first)
    print('second min is',second)
arr=[12,13,1,10,34,1]
fun(arr,len(arr))