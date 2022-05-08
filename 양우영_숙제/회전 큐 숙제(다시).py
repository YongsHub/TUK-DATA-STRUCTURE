import sys
from collections import deque
n, m= map(int,input().split())
number = list(map(int,input().split()))#뽑아내려고 하는 수의 위치를 번호대로 담는다.
data = deque([i for i in range(1,n+1)])#deque([1,2,3,4,5,6,7,8,9,10])으로 큐로 표현한다.

count = 0
for num in number:
    while 1:
        if data[0] == num:
            data.popleft()
            break
        else:
            if data.number(num) <= len(data)//2: #길이를 2로 나눈 몫이 작거나 같으면 
                data.rotate(-1)#왼쪽으로 이동시킨다.
                count += 1
            else:
                data.rotate(1)#오른쪽으로 이동한다.
                count += 1

print(count)
