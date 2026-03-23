'''
메모

N: N자리 숫자
K: 지울 수 있는 개수


지울 수 있는 경우
1) 뒷 숫자가 더 클때
2) 지울 수 있는 카운트가 남아있을 때

** 관건: 이미 앞에 여러 개의 숫자가 있는데, 두 숫자가 모두 작을 경우, 여러번 비교해서 지워야함.
** 예외 케이스: 모두 다 똑같은 숫자가 들어왔을 때?
'''
from collections import deque


N, K = map(int, input().split())
num = input()

# N, K = 4, 3
# num = str(5555)

stack = deque()
stack.append(num[0])
# print(stack)

for idx in range(1, N):
    # print("현재 처리중인 idx: ", idx, '-> 실제 숫자: ', num[idx], '현재 K: ', K)
    while stack and K > 0:
        if stack[-1] < num[idx]:
            # print('경우 1: 앞 숫자보다 큼!')
            stack.pop()
            K -= 1
        else:
            # print('경우 2: 앞 숫자보다 작음')
            break
    stack.append(num[idx])
    # print(stack, "현재 K: ", K)
    # print('\n')

if K > 0:
    print(int("".join(stack)[:len(stack)-K]))
else:
    print(int("".join(stack)))


'''
[문제에서 더 고려했어야 했던 것들]
1. 예외 케이스
이 문제 같은 유형 (숫자를 처리해야 하는 유형)
- 완전 오름차순: K가 부족하고, 연속적으로 지우는 것이 필요했음 -> for 문이 아니라 while문을 사용한 이유
- 완전 내림차순: K가 다 소진이 안되었을 것임
- 전부 같은 숫자: K가 다 소진이 안되었을 것임

2. 자료구조로 stack을 써야 했던 이유
- 앞자리 숫자를 지울지말지는, 뒤에서 들어오는 숫자가 결정함

3. While문 잘 쓰는 방법! -> 다시 비교해야하는 문제라 while문을 썼어야 했음
- 이 while은 "반복"이 논리적으로 맞는가?
- 한번 pop하고 끝나면 안되는 것인가?
- pop한 후에 다시 비교해야 하는가?
- 그리고 pop을 했을 때 stack이 비어있는 경우가 발생하는가?

위와 같은 내용을 확인해서 적용했어야 함.
'''