
string = input()    #입력 받은 문자열 (ex) mirkovC4nizCC44
bomb=input()        #폭발 문자열      (ex) C4

last= bomb[-1]      #폭발 문자열의 마지막 문자 ( => '4')
stack=[]        
b_length=len(bomb)  #폭발 문자열의 길이 ( => 2)

for c in string:
  stack.append(c)   #스택 삽입
  if c == last and ''.join(stack[-b_length:]) == bomb:
  #입력 받은 문자열에서 c == 폭발 문자열의 마지막 문자('4')
  #스택의 끝부터 폭발 문자열의 길이만큼의 문자열 == 폭발 문자열
  #(ex) ''.join(stack[-2:]) == bomb
    del stack[-b_length:]
    #스택의 끝부터 폭발 문자열의 길이만큼의 문자열 삭제
    
answer=''.join(stack)
#스택의 남은 문자열 합치기

if answer == '':  #stack이 비어있으면
  print("FRULA")
else:
  print(answer)

#(ex)''.join(stack[-2:]) => "44"
#(ex)''.join(stack[-2:]) => "C4" -> (삭제) => mirkovC4nizC(__)4
#(ex)''.join(stack[-2:]) => "C4" -> (삭제) => mirkovC4niz(__)
#                ...
#(ex)''.join(stack[-2:]) => "C4" -> (삭제) => mirkov(__)niz
#                ...
#(ex)''.join(stack) => "mirkovniz"