from sys import maxsize
def maxmin(arr,n):
    first=maxsize
    second=maxsize
    for i in range(0,n):
        if arr[i]<first:
            second=first
            first=arr[i]

        elif arr[i]<second and first!=arr[i]:
            second=arr[i]

    print('min is',first)
    print('second min is',second)
arr=[12,13,1,10,34,1]
maxmin(arr,len(arr))
