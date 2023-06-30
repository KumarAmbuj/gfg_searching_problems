def findpair(arr,n,sum):

    for j in range(1,n):
        i=j-1
        key=arr[j]
        while(i>=0 and key<arr[i]):
            arr[i+1]=arr[i]
            i=i-1
        arr[i+1]=key



    i=0
    j=1
    while i<n and j<n:
        if i!=j and arr[j]-arr[i]==sum:
            print('( {} and {} )'.format(arr[i],arr[j]))
            return True
        elif arr[j]-arr[i]<sum:
            j=j+1
        else:
            i=i+1
    return False
arr = [1, 8, 30, 40, 100]
r=findpair(arr,len(arr),60)

