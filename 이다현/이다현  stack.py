#push 숫자 를 입력받으면, len을 이용해서 배열의 길이를 파악한 후 길이-1의 인덱스 자리에 값 넣기
#pop 배열 길이 파악후 마지막에 있는 값을 빼서 출력한다. 배열의 길이가 0이면 -1출력
#size len을 이용해서 stack 배열길이 파악
#empty len을 이용해서 stack 배열이 비어있는지 확인
#top 배열의 0의 자리에 있는 숫자 출력, 비어있으면 -1출력

import sys

num = int(sys.stdin.readline())
stack = []

for i in range(num):
    fun = sys.stdin.readline().split()
    if fun[0] == "push":
        stack.insert(len(stack), fun[1])

    elif fun[0] == "pop":
        if len(stack) != 0: print(stack.pop())
        else : print(-1)

    elif fun[0] == "size":
        print(len(stack))

    elif fun[0] == "empty":
        if len(stack) == 0: print(1)
        else : print(0)

    elif fun[0] == "top":
        if len(stack) == 0:print(-1)
        else : print(stack[len(stack)-1])
