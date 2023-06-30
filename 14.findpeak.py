def findpeak(arr,n):
    for i in range(1,n-1):
        if arr[i]> arr[i-1] and arr[i]>arr[i+1]:
            print(arr[i])
arr=[10, 20, 15, 2, 23, 90, 67]
findpeak(arr,len(arr))