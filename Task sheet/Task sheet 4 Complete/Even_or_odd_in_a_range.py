minirange=minirange1=int(input("Enter the minirange "))
maxrange=maxrange1=int(input("Enter the value of maximum number: "))
print("EVEN numbers are:")
for minirange in range(minirange,maxrange+1):
	if minirange%2==0:
		print(minirange)
		minirange+=1
	else:
		pass
print("ODD numbers are:")
for minirange1 in range(minirange1,maxrange1+1):
	if minirange1%2!=0:
		print(minirange1)
		minirange1+=1
	else:
		pass
