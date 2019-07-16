# cook your code here

for _ in range(int(raw_input())):
    C,D,L = map(int,raw_input().split())
    MaxVal=C*4 + D*4
    if C>2*D:
        MinVal=MaxVal - 2*D*4
    else:
        MinVal=D*4
    if L>=MinVal and L<=MaxVal and L%4==0:
        print 'yes'
    else:
        print 'no'
    
