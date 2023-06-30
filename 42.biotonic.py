def fun(arr,n):
    left=[0]*n
    right=[0]*n
    for i in range(1,n):
        if arr[i]>arr[i-1]:
            left[i]=left[i-1]+1


    for i in range(n-2,-1,-1):
        if arr[i]>arr[i+1]:
            right[i]=right[i+1]+1

    sum=0
    index=0
    for i in range(n):
         if left[i]+right[i]>sum:
             sum=left[i]+right[i]
             index=i
    return index
arr= [5, 1, 4,5,6,7,8,6,5,3,2,1]
result=fun(arr,len(arr))
print(result)


