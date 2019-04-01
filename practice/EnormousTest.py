# Solution to https://www.codechef.com/problems/INTEST
n,k= input().split()
n= int(n)
k= int(k)
a=list()

for i in range(n):
    a.append(int(input()))

j=0

for i in range(n):
    if a[i]%k==0:
        j+=1
    
print(j)
    