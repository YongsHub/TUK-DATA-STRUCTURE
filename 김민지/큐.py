import sys
input = sys.stdin.readline

n = int(input())
queue = []
command = []
for i in range(n):
    command = input().split()
    if command[0] == "push":
        queue.append(command[1])
    elif command[0] == "pop":
        if not queue:
            print(-1)
        else:
            print(queue.pop())
    elif command[0] == "size":
        print(len(queue))
    elif command[0] == "empty":
        if not queue:
            print(1)
        else:
            print(0)
    elif command[0] == "front":
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif command[0] == "back":
        if not queue:
            print(-1)
        else:
            print(queue[-1])
    else:
        print("명령이 잘못되었습니다.")
        i-=1           #고치고 싶은 점: 명령이 잘못되었을 경우 i를 하나 뒤로 하고 싶은데 안돼요...
