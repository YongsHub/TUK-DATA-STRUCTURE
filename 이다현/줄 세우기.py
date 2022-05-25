#첫 번째 학생부터 번호를 뽑는다.
#뽑은 번호를 순서대로 리스트에 정리해.
#순서대로 넣어.
#순서대로 출력해.

import sys

num = int(input())
pick = list(map(int, input().split()))  #순서대로 리스트에 정리
answer = []

#예시로 0 1 1 3 2
#출력이 4 2 5 3 1

for i in range (num):                   #주어진 숫자만큼 반복해서
    answer.insert(i-pick[i], i+1)       #insert를 이용해서 원하는 자리에 원하는 숫자를 넣는다.

for i in range (num):                   #주어진 숫자만큼 반복해서
    print (answer[i], end=' ')          #하나씩 프린트해서 숫자사이에는 공백만 두기
