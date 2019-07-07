import sys

# 1 4 3 2

while True:
	t=raw_input()
	t=int(t)
	if t==0:
		sys.exit()
	arr=[]
	ans='ambiguous'
	arr= raw_input().split()
	arr= [0] + arr
	for i in range(1,t+1):
		if(i==int(arr[int(arr[i])])):
			continue;
		else:
			ans='not ambiguous'
			break;
	print(ans)
