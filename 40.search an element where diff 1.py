def find(arr,n,x):
    i=0
    while(i<n):

        if arr[i]==x:
            return i
        i=i+abs(arr[i]-x)
arr = [8 ,7, 6, 7, 6, 5, 4, 3, 2, 3, 4, 3 ]
i=find(arr ,len(arr),3)
print(i)