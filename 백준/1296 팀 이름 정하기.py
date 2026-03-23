'''
문제 정리

input:
연두의 영어 이름, 팀 이름 후보 개수 N,  N개의 후보 이름
output:
우승할 확률이 가장 높은 팀 이름
만약, 확률이 가장 높은 팀이 여러개일 경우, 사전 순으로 가장 앞서는 팀 이름이 우승할 확률이 가장 높음
'''
from collections import defaultdict

# print([a for a in Name])

NAME = input() # 연두의 영어 이름
N = int(input()) # 후보 개수
candidates = [input() for __ in range(N)]

results = defaultdict()
# 하나씩 비교하는 방법

best_prob = -1
best_name = ''

for c in candidates:
    count_LOVE = []
    for alph in ['L', 'O', 'V', 'E']: # 연두의 이름과 같은 알파벳 개수 세기
        count_LOVE.append(c.count(alph)+NAME.count(alph))
    # print(f"candiate - {c}: {count_alphabet}")

    prob = 1
    for i in range(len(count_LOVE)-1): #인덱스 접근
        for j in range(i+1, len(count_LOVE)):
            # print(i, j)
            prob *= (count_LOVE[i]+count_LOVE[j])
    results[c] = prob % 100
    prob = prob % 100

    if best_prob < prob:
        best_prob = prob
        best_name = c
    elif best_prob == prob:
        if best_name > c:
            best_prob = prob
            best_name = c

print(best_name)

# results = sorted(results.items(), key=lambda x: x[1], reverse=True)
# print(results[0][0])

'''
1. 동점 조건이 나오면 -> 정렬하는 것보다 if로 비교 먼저 하는 것!
if score > best_score:
    update
elif score == best_score and name < best_name:
    update

2. 문자열 비교는 "작다(<)"가 사전순 앞임!
"A" < "B"


'''