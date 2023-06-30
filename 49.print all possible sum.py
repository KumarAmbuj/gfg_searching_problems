def fun(N):
    start=1
    end=(N+1)//2
    sum=0
    while(start<end):
        for i in range(start,end+1):
            sum=sum+i

            if sum==N:
                for j in range(start,i+1):
                    print(j,end=' ')
                print()
            if sum>N:
                break
        sum=0
        start+=1
fun(125)