def missing(list,n):
    total=(n+1)*(n+2)/2
    sum=0
    for i in range(n):
        sum=sum+list[i]

    missing=total-sum
    return missing
list=[1,2,4,5,6]
n=missing(list,len(list))
print('missing no is',n)
