from collections import Counter

T = int(input())

for t in range(1, T+1):
    num = input()
    scores = list(map(int, input().split()))

    scores.sort()
    cnt = Counter(scores)
    # print(cnt.items())

    max_key, max_value = 0, 0
    for k, v in cnt.items():
        if v >= max_value:
            max_value = v
            max_key = k


    print(f'#{num} {max_key}')