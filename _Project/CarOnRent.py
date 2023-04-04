database=dict()
stock=int(50)
l=[]
while True:

	userid=input('Enter your id: ')
	if userid not in database:
		print()
		custnum=input('Enter your mobile number:')
		print('''
		Welcome to car rental company
		 1. Rent a car
		 3. Exit

		Available cars = ''',stock)
		choice=int(input('Enter your choice:'))
		if choice==1:
			print("PRICE OF 1 CAR @RS.500/DAY")
			confrmatn = input("DO YOU WANT TO CONFIRM CAR BOOKING(yes/no): ")
			if confrmatn == "yes":
				qnt = int(input("ENTER THE NUMBER OF CARS FOR RENT: "))
				if qnt<=stock:
					days = input("FOR HOW MANY DAYS DO YOU NEED CAR: ")
					name = input("ENTER YOUR NAME: ")
					cnum = input("ENTER YOUR CONTACT NUMBER: ")
					l.append(days)
					l.append(name)
					l.append(cnum)
					database[userid]=l
					# Cid = input("ENTER YOUR ID: ")
					bill=open(userid,"bill.txt","x")
				elif qnt>stock:
					print("SORRY!",qnt,"CARS ARE'NT AVAILABLE AT THIS MOMENT")
