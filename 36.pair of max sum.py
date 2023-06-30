def product(arr,n):
    posa=0
    posb=0

    nega=0
    negb=0

    for i in range(n):
        if arr[i]>posa:
            posb=posa
            posa=arr[i]
        elif arr[i]>posb:
            posb=arr[i]


        if arr[i]<0 and abs(arr[i])>abs(nega):
            negb=nega
            nega=arr[i]
        elif arr[i]<0 and abs(arr[i])>abs(negb):
            negb=arr[i]
    if posb*posa>negb*nega:
        print('max product {} and {} '.format(posa,posb))
    else:
        print('max product {} and {}'.format(nega,negb))

arr = [1, 4, 3, -6, -7, 0]
product(arr,len(arr))
