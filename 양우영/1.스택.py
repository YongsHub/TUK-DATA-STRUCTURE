import sys #sys모듈은 파이썬 인터프린터가 제공하는 변수와 함수를 직접 제어할수 있게 해주는 모듈이다

Number = int(sys.stdin.readline()) #sys.stdin.readline()는 sys 모듈의 파일 객체 stdin의 매소드 중 readline()을 사용한다는 의미

stack = [] #스택 리스트를 만들어 준다

for i in range(Number):
    string = sys.stdin.readline().split() #split함수를 사용하면 띄어쓰기,엔터를 구분하여 문자열을 나누게 된다. 
    command = string[0] #명령어을 받을수 있도록 함수를 만듬

    if command == "push":# 명령어가 push라면
        value = string[1]# ex) push 2-> string[0]=명령어,string[1]=2를 말한다.
        stack.append(value)#ex) 2값을 스택 리스트에 추가한다.

    elif command == "pop":# 명령어가 pop라면
        if len(stack)==0:#스택 리스트에 아무것도 없다면 -1을 출력하고 아니라면 pop을한다
            print(-1)
        else :
            print(stack.pop())#여기서 pop은 sys모듈 안에 있어서 그냥 괜찮다.

    elif command == "size" :# 명령어가 size라면 리스트안에 들어있는 정수의 개수를 출력한다.
        print(len(stack))

    elif command == "empty" :# 명령어가 empty라면 리스트안에 아무것도 없을때에는 1을 출력하고 아니면 0을 출력한다.
        if len(stack)==0:
            print(1)
        else :
            print(0)
    elif command =="top":#명령어가 top이라면 리스트에 값이 없다면 -1을 출력하고 아니라면 제일 오른쪽 값 즉, 스택의 가장 위에 있는 정수를 출력한다.
        if len(stack)==0:
            print(-1)
        else :
            print(len(stack)-1) #제일 오른쪽 값
            
