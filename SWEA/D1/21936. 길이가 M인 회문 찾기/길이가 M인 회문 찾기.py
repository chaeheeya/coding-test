T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    str = input()

    found = False
    for i in range(N):
        current = str[i]
        cnt = 1
        for j in range(i+1, N):
            cnt += 1
            if str[j] == current and j-i+1 == M:
                found = True
                answer = str[i:i + M]
                print(f'#{t} {answer}')
                break

        if found:
            break

    if not found:
        print(f'#{t} NONE')

