# cook your code here

#raw_input().split() always for an array
for _ in range(int(raw_input())):
    n = int(raw_input())
    N = map(int,raw_input().split())
    f = int(raw_input())
    F = map(int,raw_input().split())
    if f>n:
        print 'No'
        continue
    i,j = 0,0
    while i<f and j<n:
        if F[i]==N[j]:
            i+=1
        j+=1
    if i==int(f):
        print 'Yes'
    else:
        print 'No'
