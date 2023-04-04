marks=int(input("Enter the student marks: "))
if marks<=50:
	print("3rd devision")
elif marks>=50 and marks <=70:
	print("2nd devision")
elif marks>70:
	print("1st devision")
else:
	print("Error! only int value accepted")