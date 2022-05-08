from collections import deque

N,pick=map(int,input().split())
lst=deque(range(1,N+1))              # 1,2,3,4,5,...,n+1
q=deque(map(int,input().split()))    # q = 뽑을 위치
count=0
while q:
  mid=len(lst)//2
  if lst.index(q[0])>mid:
    while q[0]!=lst[0]:
      lst.appendleft(lst.pop)
      count+=1
      




    else:
      