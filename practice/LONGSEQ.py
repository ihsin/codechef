# cook your code here
t = int(raw_input())
for _ in range(t):
    num = raw_input().strip()
    one=0
    zero=0
    for char in num:
        if char=='1':
            one+=1
        else:
            zero+=1
    if one==1 or zero==1:
        print 'Yes'
    else:
        print 'No'
