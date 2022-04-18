import sys
input = sys.stdin.readline  #시간 절약; sys.stdin.readline()의 출력값은 문자열; 형 변환 필요; 개행문자(\n)도 포함

n = int(input())    # sys.stdin.readline()-한개의 정수를 입력받을 경우
stack = []
command = []        #궁금한 점: split() 자체가 리스트를 만드는데 command리스트가 따로 필요할지
for i in range(n):
    command = input().split()   #n줄의 문자열을 입력받아 리스트에 저장할 경우
    if command[0] == "push":
        stack.append(command[1])
    elif command[0] == "pop":
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == "size":
            print(len(stack))
    elif command[0] == "top":
        if not stack :
            print(-1)
        else:
            print(stack[-1])
    elif command[0] == "empty":
        if not stack:
            print(1)
        else:
            print(0)
