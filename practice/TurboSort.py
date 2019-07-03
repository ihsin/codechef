#https://www.codechef.com/problems/TSORT
t= input()
t= int(t)

arr= list()

for i in range(0,t):
    arr.append(int(input()))

arr.sort()

for i in arr:
	print(i)
