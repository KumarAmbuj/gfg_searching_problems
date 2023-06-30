def fun(arr1,arr2,sum):
    n1=len(arr1)
    n2=len(arr2)
    l=0
    r=n2-1
    diff=67865
    resl=0
    resr=0

    while(l<n1 and r>=0):
        if abs(arr1[l]+arr2[r]-sum)<diff:
            resl=l
            resr=r
            diff=abs(arr1[l]+arr2[r]-sum)

        if arr1[l]+arr2[r]<sum:
            l=l+1
        else:
            r=r-1

    print('two nos {} and {} '.format(arr1[resl],arr2[resr]))
arr1 = [1, 4, 5, 7]
arr2 = [10, 20, 30, 40]
fun(arr1,arr2,38)
