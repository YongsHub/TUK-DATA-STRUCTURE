
string = input()
bomb = input()

stack = []
lastChar = bomb[-1]
length = len(bomb)


for i in string:                #O(n)
    stack.append(i)        
    if length <= len(stack) and i == lastChar and ''.join(stack[-length:]) == bomb:   #stack리스트 뒤에서부터 length개가 bomb와 같으면 
        del stack[-length:]

answer = ''.join(stack)

if answer == '':
    print("FRULA")
else:
    print(answer)
