t= input()
t= int(t)

arr= list()

for i in range(t,0,-1):
    arr.append(input())

arr.sort()

for i in arr:
    print(i)