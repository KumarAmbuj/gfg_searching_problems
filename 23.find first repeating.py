def findfirstrepeating(arr,n):
    for i in range(n):
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    print(arr)

    temp=[0]*(n)

    for i in range(len(arr)):
        if temp[arr[i]]==0:
            temp[arr[i]]==
arr = [10, 5, 3, 4, 3, 5, 6]
findfirstrepeating(arr,len(arr))