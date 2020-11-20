# This code generates the fibonacci serie from 1 to 1000
# This single line set a = b and in that point b = 0; then set b = 1
a,b=0,1
while b<1000:
#	print("a="+str(a)),
#	print("b="+str(b)),
#	print("a+b="+str(a+b)),
	print(b),
	a,b=b,a+b,
