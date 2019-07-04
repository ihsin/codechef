n=input()
n=int(n)

cumulative1=0
cumulative2=0
winner=1
absDiff=-999999

for i in range(n):
	score1,score2= raw_input().split()
	score1= int(score1)
	score2= int(score2)
	cumulative1+=score1
	cumulative2+=score2
	diff=cumulative1-cumulative2
	if(absDiff<abs(diff)):
		absDiff=abs(diff)
	if(abs(diff)==absDiff):
		if(diff<0):
			winner=2
		else:
			winner=1
print(winner),
print(absDiff),
