t= raw_input()
t= int(t)


for i in range(t):
	n= raw_input()
	l= len(n)
	L=l-1
	ans=0
	for j in range(l):
		n= int(n)
		x= n%10
		x*=10**L
		n=n/10
		ans+=x
		L-=1
	print(ans)	
