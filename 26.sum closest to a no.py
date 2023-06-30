def fun(arr,n,sum):
    diff=8989
    l=0
    r=n-1
    resl=0
    resr=0
    while(l<r):
        if abs(arr[l]+arr[r]-sum)<diff:
            diff=abs(arr[l]+arr[r]-sum)
            resl=l
            resr=r


        if arr[l]+arr[r]<sum:
            l=l+1
        else:
            r=r-1
    print('closest sum is {} and {} '.format(arr[resl],arr[resr]))
arr = [10, 22, 28, 29, 30, 40]
fun(arr,len(arr),54)
