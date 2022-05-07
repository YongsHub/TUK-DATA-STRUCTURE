#회전하는 큐

from collection import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())            #map함수 : (여기서는)int형으로 변환해서 저장
queue1 = list(map(int, input().split()))
#숫자 입력


count = 0

while 1:
    if queue1[0] == ~~~~      :   #지정한 숫자  m
        deq.popleft
    else:
        if queue1~~~~~ <= len(queue1)//2:             #남은 거리 계산............
            queue1.rotate(-1)
            count += 1
        else:
            queue1.rotate(1)
            count += 1
            
print(count)



