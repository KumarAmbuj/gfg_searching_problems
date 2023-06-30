# USING INSERTION SORT

def merge(arr1,arr2):
    n1=len(arr1)
    n2=len(arr2)
    list=[None]*(n1+n2)

    for i in range(n1):
        list[i]=arr1[i]

    k=len(arr1)-1
    i=0
    while(k<len(list) and i<n2):

        j=k
        key=arr2[i]
        while(j>=0 and key< list[j] ):
            list[j+1]=list[j]
            j=j-1
        list[j+1]=key
        i=i+1
        k=k+1
    m=len(list)//2
    return (list[m-1]+list[m])/2

result=merge([1,2,3,4],[9,5,6,7])
print(result)