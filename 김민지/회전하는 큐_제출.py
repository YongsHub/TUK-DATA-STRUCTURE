#회전하는 큐

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())            #map함수 :input을 split해서 (여기서는)int형으로 변환해서 n, m에 각각 저장
deq = deque([i for i in range(1,n+1)])      # deq = deque([1~N])
data = list(map(int, input().split()))      # 입력 받은 걸 split해서 list에 저장(입력받은 수는 아래의 for문에서 i)


count = 0

for i in data:
    while 1:
        if deq[0] == i:        #만약 deq가 data안에 있는 숫자라면.
            deq.popleft()
            break
        else:
            if deq.index(i) <= len(deq)//2:             #남은 거리 계산:현재 deq에서 i의 인덱스 번호 = i까지의 거리  
                deq.rotate(-1)
                count += 1
            else:
                deq.rotate(1)
                count += 1
            
print(count)






'''선배 코드 파악
1) answer += index   deq.rotate(-index)    deq.popleft()를 한번에 씀으로써 if문 한 번만 사용
2) while문 없음
3) find와 index를 if문 밖에서 계산'''

