no1=temp1=int(input("Enter starting number: "))
no2=temp2=int(input("Enter last number: "))

print("[prime numbers are:] ")
for i in range (no1,no2+1):
	c=2
	for j in range(2,i):
		if i%j==0:
			pass
		else:
			c=c+1
	if c==i:
		print(i,	",",end="")

print("\nNone prime numbers are:")
for i in range (temp1,temp2+1):
	c=2
	for j in range(2,i):
		if i%j==0:
			pass
		else:
			c=c+1
	if c ==i:
		print(i,",",end="")
















# no=int(input("Enter any number "))
# c=2
# for i in range (2,no):
# 	if (no%i)==0:
# 		pass
# 	else:
# 		c=c+1
# 	if c==no:
# 		print("prime")
