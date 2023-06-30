def fun(arr,n):
    temp=[0]*(n+1)
    for i in range(len(arr)):
        if temp[arr[i]]==0:
            temp[arr[i]]=1
        elif temp[arr[i]]==1:
            print('repeating term is ',arr[i])
    for i in range(1,len(temp)):
        if temp[i]==0:
            print('missiing term is ',i)

arr=[7,3,4,5,5,6,2]
fun(arr,len(arr))