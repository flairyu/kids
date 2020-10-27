import random

pcount=100
maxnum=10
for i in range(0,pcount):
    a=random.randint(0,maxnum)
    b=random.randint(0,maxnum)
    c=max(a+b,maxnum)
    d=random.randint(0,65535)%2==0
    if d:
        op='-'
    else:
        op='+'
    e=random.randint(0,3)

    if e==0:
        print('(   ) %s %d = %d' % (op, a , c), end="    ")
    elif e==1:
        if d:
            print('%d %s (   ) = %d' % (c, op, a), end="    ")
        else:
            print('%d %s (   ) = %d' % (a, op, c), end="    ")
    else:
        if d:
            print('%d %s %d = (   )' % (c, op, a), end="    ")
        else:
            print('%d %s %d = (   )' % (a, op, b), end="    ")

    if (i+1)%5==0:
        print('\r\n')
