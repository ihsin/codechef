t=input()
t=int(t)


for i in range(0,t):
	n=input()
	n=int(n)
	sum=0
	while n!=0:
		sum+=n%10
		n=n/10
	print(sum)
