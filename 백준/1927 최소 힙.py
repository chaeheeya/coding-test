import heapq
import sys

_list = []
heapq.heapify(_list)
N = int(input())

for __ in range(N):
    x = int(sys.stdin.readline())

    if x == 0:
        if not _list:
            print(0)
        else:
            print(heapq.heappop(_list))
    else:
        heapq.heappush(_list, x)


'''
1. heapq에는 숫자를 입력해줘야함
2. input()과 sys.stdin.readline()의 차이점
- input은 입력받은 값의 개행('\n') 문자를 삭제시켜 반환
값을 입력할때마다 버퍼에 저장하는 데서 오는 속도 차이
- sys.stdin.realine은 개행 문자를 포함한 값을 반환
한번에 읽어서 버퍼에 저장하고

3. 버퍼란?
- 버퍼는 컴퓨팅에서 데이터를 한 곳에서 다른 곳으로 전송할때 속도 차이를 완화하기 위해 데이터를 일시적으로 저장하는 메모리 영역 (임시 저장 공간)
- 예를 들어 영상 스트리밍으로 생각해보면, 서버에 저장된 영상 파일을 여러 조각으로 쪼개 연속적으로 데이터를 보내야함. 
여기서 버퍼는 서버로부터 보내지는 영상 파일 데이터들을 순서대로 차곡차곡 쌓는 임시 데이터 공간임.
그래서 동영상을 볼 때 밑에 재생바에 짙은 회색으로 표시된 부분이 그 버퍼를 나타냄.
'''
