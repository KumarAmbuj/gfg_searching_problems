from sys import maxsize
def Stack():
    stack=[]
    return stack
def isEmpty(stack):
    return len(stack)==0
def push(stack,item):
    stack.append(item)
def pop(stack):
    if isEmpty(stack):
        return str(-maxsize-1)
    return stack.pop()
def peek(stack):
    if isEmpty(stack):
        return str(-maxsize-1)
    return stack[len(stack)-1]
def size(stack):
    return len(stack)

def findlargest(arr,n):
    stack=Stack()

    for i in range(n):

        while not isEmpty(stack) and peek(stack)>=arr[i]:
            temp=pop(stack)

        if isEmpty(stack):
            print('-',end=' ')

        else:
            print(peek(stack),end=' ')

        push(stack,arr[i])
arr = [ 1, 3, 0, 2, 5]
findlargest(arr,len(arr))