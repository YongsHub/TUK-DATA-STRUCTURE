from collections import deque

N,pick=map(int,input().split())      # N:큐의 크기, pick:뽑으려는 숫자의 개수
lst=deque(range(1,N+1))              # 1,2,3,4,5,...,n
que=deque(map(int,input().split()))  # que = 뽑을 위치 (pick 개수 만큼)
count=0                              # 연산 횟수
while que:                      # que 참이면 반복
  mid=len(lst)//2                 # mid = lst의 가운데 숫자
  
  if lst.index(que[0])>mid:       # lst의 que 첫번째 숫자 index가 가운데 숫자보다 크면
    while que[0]!=lst[0]:           # que의 첫번째 숫자 != lst의 첫번째 숫자, 반복
      
      lst.appendleft(lst.pop())       # 3번 연산 수행 (=오른쪽으로 한칸 이동)
                                      # => 맨 오른쪽 숫자 뽑아서, 맨 왼쪽에 삽입
                                      # appendleft():왼쪽에 삽입, pop():삭제 및 뽑기
      count+=1    # 연산 +1
    lst.popleft()                   # lst의 맨 왼쪽 숫자 삭제
    que.popleft()                   # que의 맨 왼쪽 숫자 삭제
    
  else:                           # lst의 que 첫번째 숫자 index가 가운데 숫자보다 작으면
    while que[0]!=lst[0]:           # que의 첫번째 숫자 != lst의 첫번째 숫자, 반복
      
      lst.append(lst.popleft())       # 2번 연산 수행 (=왼쪽으로 한칸 이동)
                                      # => 맨 왼쪽 숫자 뽑아서, 맨 오른쪽에 삽입
                                      # append():삽입, popleft():맨 왼쪽 삭제 및 뽑기
      count+=1    # 연산 +1
    lst.popleft()                   # lst의 맨 왼쪽 숫자 삭제
    que.popleft()                   # que의 맨 왼쪽 숫자 삭제

print(count)                      # 연산 횟수 출력