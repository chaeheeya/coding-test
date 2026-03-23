'''
메모
결국 우리가 구해야하는 것은 최솟값과 최댓값

첫번째 자리애 뭐가 오느냐에 따라 달라질 것
1) 만약 '>':
최대값: 무조건 9
최소값: 무조건 1

2) 만약 '<':
최대값: ??? 뒷 조건에 따라 달라질 듯.. -> 앞에다가 숫자 끼워넣으면 안되나
최솟값: 0

'''
from collections import deque

min = deque([i for i in range(9)])
max = deque([i for i in range(1, 10)])

# k = int(input())
# P = input().split()

k = 2
P = ['<', '>']


max_result = []
max_stack = deque()
max_num = 9
for p in P:
    # 최대값 처리

    max_stack.append(max_num)
    max_num -= 1

    if p == '>':
        max_result.append(max_stack.pop())
        print(max_result)
        print(max_stack)
        print('\n')

    print(max_result)
    print(max_stack)
    print('\n')


    # 최솟값 처리