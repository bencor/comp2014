from math import log

n=int(raw_input())

#Validate first digits using extra precision
#from decimal import *
#getcontext().prec=30
#ls=0
#for i in xrange(2,n+1):
#	ls+=(i*Decimal(i).log10())%1
#	ls%=1
#print int(Decimal(10)**(ls+20))

logSum=0
logTotalSum=0
p=1
m=10**10
nb2=0
nbz=0
for i in xrange(2,n+1):
	log10=i*log(i,10)
	logSum=(logSum+(log10)%1)%1
	logTotalSum+=log10
	b=i
	while b%10==0:
		b/=10
		nbz+=i
	while b%2==0:
		b/=2
		nb2+=i
	while b%5==0:
		b/=5
		nb2-=i
		nbz+=i
	p*=pow(b,i,m)
	p%=m
if nb2>0:
	p*=pow(2,nb2,m)
else:
	#This should not happen
	p*=pow(5,-nb2,m)
	nbz+=nb2
p%=m
print int(10**min(4,int(logTotalSum-nbz))*round(10**logSum,8)), str(p).zfill(10) if logTotalSum-nbz >= 9 else p, nbz