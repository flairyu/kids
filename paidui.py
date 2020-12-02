import random

pcount=20
maxnum=10
names=['小猫','小狗','小兔子','小马','张三','李四','小红','小明','小姐姐']
for i in range(0,pcount):
    a=random.randint(0,maxnum)
    b=random.randint(0,maxnum)
    name = names[random.randint(0,len(names)-1)]
    c=random.randint(0,1)
    if c==0:
        print('%s的前面有%d个小伙伴，后面有%d个小伙伴，请问排队的一共有多少？请列式说明。'%(name, a, b))
    else:
        print('%s从前面数排在第%d，从后面数排在第%d，请问排队的一共有多少？请列式说明'%(name, a, b))

