n = int(input())
lst = list(map(int,input().split()))
line = []

for i in range(n) :
    if lst[i] == 0:
        line.insert(0,i+1)
    else :
        line.insert(lst[i],i+1)

line.reverse()
print(line)
