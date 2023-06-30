#method two using xor
# x1 contains xor of every element in list
# x2 contains xor of every index in list
def missing(list,n):
    x1=list[0]
    x2=1

    for i in range(1,n):
        x1 = x1 ^ list[i]
    print(x1)

    for i in range(2, n+2):
        x2 = x2 ^ i
    print(x2)

    x= x1 ^ x2
    return x
list=[1,2,4,5,6]
n=missing(list,len(list))
print(n)