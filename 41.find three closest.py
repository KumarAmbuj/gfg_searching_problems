def fun(arr1,arr2,arr3):
    n1=len(arr1)
    n2=len(arr2)
    n3=len(arr3)

    i=0
    j=0
    k=0

    diff=9090
    resi=0
    resj=0
    resk=0
    while(i<n1 and j<n2 and k<n3):

        mx=max(arr1[i],max(arr2[j],arr3[k]))
        mn=min(arr1[i],min(arr2[j],arr3[k]))

        if mx-mn<diff:
            resi=i
            resj=j
            resk=k
            diff=mx-mn

        if diff==0:
            break

        if arr1[i]==mn:
            i=i+1
        elif arr2[j]==mn:
            j=j+1
        else:
            k=k+1
    print('{}, {} and {}'.format(arr1[resi],arr2[resj],arr3[resk]))
A = [1, 4, 10]
B = [2, 15, 20]
C = [10, 12]
fun(A,B,C)

