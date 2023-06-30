def fun(list,x):
    count=0
    for i in range(len(list)):
        if list[i]==x:
            count+=1
    print(count)
ar=[1,2,2,2,2,3,4,7,8,8]
fun(ar,2)