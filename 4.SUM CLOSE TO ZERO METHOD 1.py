# FINDING SUM OF EACH ELEMENT WITH OTHER
#WHEN WE FIND MIN WE PRINTOUT
def fun(arr,n):
    sum=8907
    l=[]
    for i in range(n):
        for j in range(i+1,n):

            if abs(arr[i]+arr[j])<sum:
                sum=abs(arr[i]+arr[j])
                l.append(arr[i])
                l.append(arr[j])

    print('{} and {}'.format(l.pop(),l.pop()))
arr=[1,60,-10,70,-80,85]
fun(arr,len(arr))