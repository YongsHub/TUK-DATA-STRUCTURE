import sys

#join개념
#a = [1, 2, 3, 4, 5]가 있을때,
#''.join(a) 라고 하면, 12345로 출력됨.
#''.join(a[-2:]) 라고 하면, 뒤에서 두번째부터 끝까지 45로 출력됨.

string = input()      #전체 문자열 string 받기
bomb = input()        #bomb 문자열 받기
lastchar = bomb[-1]   #bomb 문자열의 마지막 문자 넣기
stack = []            #스택 생성
length = len(bomb)    #length에 bomb의 글자 수를 넣어줌.

for i in string:
    stack.append(i)     #for문이 돌면서 stack에 한글자씩 넣기
    if i == lastchar and bomb == ''.join(stack[-length:]):
        #들어간 문자가 bomb의 마지막 문자가 같은지 확인하고,
        #bomb만큼의 문자개수만큼 뽑아와서 확인.
        del stack[-length:]

if not stack:
    print("FRULA")
else:
    print(''.join(stack))
