#merge two sotrted array first then find median

def findmedian(arr1,arr2):

    if arr1[0]>arr2[len(arr2)-1]:
        for i in range(len(arr1)):
            arr2.append(arr1[i])

        print(arr2)
        m=len(arr2)//2
        print(m)
        return (arr2[m-1]+arr2[m])/2


    if arr2[0] >= arr1[len(arr1) - 1]:
        for i in range(len(arr2)):
            arr1.append(arr2[i])
        m = len(arr1)//2
        print(m)
        print(arr1)
        return (arr1[m-1]+arr1[m])/2

    i=0
    j=0
    n1=len(arr1)
    n2=len(arr2)
    list=[]
    while(i<n1 or j<n2):
        if arr1[i]<=arr2[j]:
            list.append(arr1[i])
            i=i+1
            if i==n1:
                break


        else:
            list.append(arr2[j])
            j=j+1
            if j==n2:
                break

    if i<n1:
        while(i<n1):
            list.append(arr1[i])
            i=i+1
    if j<n2:
        while(j<n2):
            list.append(arr2[j])
            j=j+1
    print(list)

    m=(n1+n2)//2

    return (list[m-1]+list[m])//2
ar1 = [1, 12, 15, 26, 38]
ar2 = [2, 13, 17, 30, 45]
result=findmedian(ar1,ar2)
print(result)

