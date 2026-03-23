N, M = map(int, input().split(' '))
S = set()
for __ in range(N):
    string = input()
    S.add(string)

answer = 0
for __ in range(M):
    input_string = input()
    if input_string in S:
        answer +=1

print(answer)

'''
예외상황 및 주의사항
1. 비교당하는 대상은 하위 M개의 문자열들임. 그 말은 즉, 상위 N개의 문자열은 중복 저장할 필요가 없다는 것임.
그렇기 때문에 list를 사용할게 아니라, set을 사용해서 메모리를 아낄 수 있음.
그리고 저장은 N에 대해서만 하고 M은 하나씩 입력을 받으면서 N에 있는지 없는지만 확인하면 되는 문제!

2. 그리고 문제를 잘 읽으면, 포함되는 문자열을 고르는게 아니라 매칭되는 문자열을 고르는 것임.
그래서 in 이 아니라, == 으로 실제로 매칭되는 문자열이 존재하는지를 확인해야함.

'''