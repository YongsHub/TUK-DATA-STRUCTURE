import sys 

Number = int(sys.stdin.readline()) 

queue = [] 

for i in range(Number):
    string = sys.stdin.readline().split() 
    command = string[0] 

    if command == "push":
        value = string[1]
        queue.insert(0,value) #ex)1,2,3,4를 차례대로 입력한다고 한다면 큐는 4->3->2->1순으로 왼쪽(앞)에서 차례대로 출력이 된다.

    elif command == "pop":#스택과 같은 방식
        if len(queue)==0:
            print(-1)
        else :
            print(queue.pop())


    elif command == "size" :#스택과 같은 방식
        print(len(queue))


    elif command == "empty" : #스택과 같은 방식
        if len(queue)==0:
            print(1)
        else :
            print(0)

    elif command =="front":
        if len(queue)==0:
            print(-1)
        else:
            print(queue[len(queue)-1]) #만약 차례대로 1(맨위큐[0]),2,3,4(맨아래queue[3])가 있다고 하자,큐는 먼저 들어온것이 먼저 나가기 때문에   
                                       #사실상 4가 가장 앞에 있는 정수이다.따라서 queue[3]이 출력 되기 위햐서는 큐 리스트의 길이에 -1이 나온다.
    elif command =="back":
        if len(queue)==0:
            print(-1)
        else:
            print(queue[0])            #위와 같이 맨위에 있는 1이 사실상 가장 뒤에 있는 정수 이기 때문에 queue[0]을 출력하면 된다.
        
 
            
