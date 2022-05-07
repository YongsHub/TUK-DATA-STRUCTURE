import sys
from collections import deque #deque import해서 사용해주기

Max, Num = map(int, input().split()) #뽑을 숫자의 개수와, deque의 개수 받기

deq = deque([i for i in range(1, Max+1)])

output = [int(x) for x in input().split()] #공백으로 나누어진 ?개의 정수를 리스트로 만들어준다.
count = 0

#자 다 입력을 받았어 이제 정리해줘야지 그치?
#1번 for 문을 Num만큼 돌게 해
for i in range(Num): #주어지는 정수의 개수만큼 돈다.
    out_num = output[i]  #첫번째로 뽑아낼 정수
    index = deq.index(out_num)
    if index <= len(deq)-index:
        count += index
        deq.rotate(-index)
        deq.popleft()
    else:
        count += (len(deq)-index)
        deq.rotate(len(deq)-index)
        deq.popleft()
print (count)
