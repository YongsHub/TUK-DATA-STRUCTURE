A=int(input())#학생의 수
number=list(map(int,input().split()))#list(map(함수,리스트))사용,학생들이 뽑은 번호
lst=[]

for i in range(A):
    lst.insert(i-number[i],i+1)

for j in lst:
    print(j,end=' ')#end=' ' 가 없게 된다면 결과값이 가로 한줄이 아니라 세로로 출력된다

#줄은 선 학생들(만약 5명이라고 할때 1,2,3,4,5)이 0,1,2를 뽑아 다시 최종적으로 줄을 세운다.
