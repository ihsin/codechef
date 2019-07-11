# cook your code here
t= raw_input()
t= int(t)

for _ in range(t):
        N,K= map(int,raw_input().split())
        max=0
        for i in range(1,K+1):
            if(N%i>=max):
                max=N%i
        print(max)
