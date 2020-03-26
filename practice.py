# 生成等差数列或多组混合等差数列
# 使用方式：
# python3 practice.py 12
# 将会生成12组测试题
import random
import sys

def generateList(L):
    N = random.randint(1,3)
    R = {}
    for i in range(0, N):
        R[i] = {'value':random.randint(1,5), 'step':random.randint(1,10)}
    for i in range(0, L):
        for j in range(0,N):
            print(R[j]['value'], ",", end = '')
            R[j]['value'] += R[j]['step']
    print('___, ___, ___')

def main(argv):
    M = int(argv[0]) if len(argv)>0 else 10
    for m in range(0, M):
        generateList(6)

if __name__ == "__main__":
    main(sys.argv[1:])