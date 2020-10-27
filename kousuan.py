import random

pcount=100
maxnum=10
for i in range(1,pcount):
   a=random.randint(0,maxnum)
   b=random.randint(0,maxnum)
   c=max(a+b,maxnum)
   d=random.randint(0,65535)%2==0
   if (d):
      op='-'
   else:
      op='+'
   e=random.randint(0,3)
   if (e==0):
       print('(   )'+op+a+'='+c
   elif (e==1):
       print(c+op+'(   )='+a
   else:
       print(c+op+a+'=(   )'
   if (i%5==0):
       print('\r\n')
   else:
       print('    ')



