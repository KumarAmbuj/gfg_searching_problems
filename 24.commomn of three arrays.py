def common(arr1,arr2,arr3):
    i=0
    j=0
    k=0
    n1=len(arr1)
    n2=len(arr2)
    n3=len(arr3)
    while(i<n1 and j<n2 and k<n3):

        if arr1[i]==arr2[j] and arr2[j]==arr3[k]:
            print(arr1[i],end=' ')
            i+=1
            j+=1
            k+=1

        elif arr1[i]<arr2[j]:
            i=i+1
        elif arr2[j]<arr2[k]:
            j=j+1
        else:
            k=k+1
arr1 = [1, 5, 10, 20, 40, 80]
arr2 = [6, 7, 20, 80, 100]
arr3 = [3, 4, 15, 20, 30, 70, 80, 120]
common(arr1,arr2,arr3)