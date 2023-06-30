def fun(arr,n):
    for i in range(len(arr)):
        if arr[i]==i:
            print(arr[i])
arr = [-10, -1, 0, 3, 10, 11, 30, 50, 100]
fun(arr,len(arr))