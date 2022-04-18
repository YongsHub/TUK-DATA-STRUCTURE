#push 숫자 를 받으면, insert를 이용해서 배열의 제일 앞에 값 넣기
#pop if문으로 배열의 길이가 0이라면 -1 출력, else면 배열[0]값 빼서 출력.
#size len함수로 queue 배열의 길이 알려주기. 
#back : if문으로 배열의 길이가 0이라면 -1 출력, else면 배열[0]값 출력하기
#front : if문으로 empty를 이용해서 -1 출력, else면 len함수 이용해서
#크기 구해주고, 거기서 -1한 숫자의 인덱스를 가지고 있는 값 출력.

import sys
num = int(sys.stdin.readline())
queue = []

for i in range(num):
    fun = sys.stdin.readline().split()
    #input로 입력받으면 시간초과됨.
    if fun[0] == "push":
        queue.insert(0, fun[1])

    elif fun[0] == "pop":
        if len(queue) != 0:print(queue.pop())
        else: print(-1)

    elif fun[0] == "size":
        print(len(queue))

    elif fun[0] == "empty":
        if len(queue) == 0: print(1)
        else : print(-1)

    elif fun[0] == "front":
        if len(queue) == 0: print(-1)
        else : print(queue[len(queue)-1])

    elif fun[0] == "back":
        if len(queue) == 0:print(-1)
        else : print(queue[0])
