# cook your code here
#1 4 2 3
for _ in range(int(raw_input())):
    n= int(raw_input())
    arr= map(int,raw_input().split())
    start=0
    end=1
    count=0
    while start<end and end<n:
        if arr[end]>=arr[end-1]:
            end+=1
        if end==n or arr[end]<arr[end-1]:
            x=end-start
            count+= x*(x-1)/2
            start=end
            end+=1
    print (n+count)
