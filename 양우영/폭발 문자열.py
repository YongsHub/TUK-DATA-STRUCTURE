import sys
input = sys.stdin.readline #한줄에 여러 입력값들을 받을수 있음 

input_string = list(input().rstrip()) #문자열과 폭탄 문자열 입력을 구분자.join(리스트)대신에 .rstrip함수를 사용하여 공백을 없애 문자열을 합침
bomb_string= list(input().rstrip())

stack =[] #리스트를 만듦

for i in range(len(input_string)): #입력 문자열의 수만큼 반복한다
    stack.append(input_string[i])#입력 문자열을 stack으로 넣는다
    if stack[-1]==bomb_string[-1] and len(stack) >=len(bomb_string):#뒤부터 탐색하여 마지막 문자열이 같고 길이가 폭탄 문자열보다 크다면 실행
        if stack[-len(bomb_string):] == bomb_string: #뒤부터 탐색하여 찾은 스택 문자열과 폭탄 문자열이 같다면
            for i in range(len(bomb_string)):#폭탄 문자열의 길이만큼 삭제함
                stack.pop()
        
answer = ''.join(stack) #답은 .join(리스트)사용하여 문자열을 합침

if answer == "":
    print("FRULA")
else:
    print(answer)



#m(-15)i(-14)r(-13)k(-12)o(-11)v(-10)C(-9)4(-8)n(-7)i(-6)z(-5)C(-4)C(-3)4(-2)4(-1)
#만약 입력 문자열의 맨뒤와 폭탄의 문자열이 같음 ->stack[-2:]==C4?->아님-> 다시 탐색 ->다시 입력 문자열과 폭탄문자열의 마지막 문자열이 같음->stack[-2:]==C4?->C4를 삭제->다시 탑색하고 삭제하고
# 최종적으로 폭탄문자열과 같은 입력문자열이 없다면 해덩 결과값을 asnwer에 넣음

    
