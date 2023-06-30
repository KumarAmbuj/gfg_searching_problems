def fun(list,low,high,x):
    if x<list[low]:
        return low
    for i in range(low,high):
        if x==list[i]:
            return i

        if (list[i]<x and list[i+1]>x):
            return i+1
    return -1

arr=[1,2,8,10,10,12,19]
index=fun(arr,0,len(arr)-1,3)
if index==-1:
    print('ceiling doesnot exist')
else:
    print('ceiling of x is',arr[index])

