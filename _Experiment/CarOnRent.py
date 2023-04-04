

def bill_gen(*args):
	data=f'''
	WELCOME TO CAR RENTAL COMPANY-------
	NAME : {args[0]}
	phone: {args[1]}
	user id:{args[2]}
	no of car: {args[3]}
	Days: {args[4]}
	Amut: {args[5]}
	'''
	bill=args[0]+".txt"
	p=open(bill,'w')
	p.write(data)
	p.close()
	print("Thanks for purchase Don't forget to take BILL....")

# database=dict{}
database ={'0000':[2,'Nametemp','number',]}
stock=int(50)
l=[]
while True:
	userid=input('Enter your id: ')
	if userid not in database:
		print()
		print('''
		Welcome to car rental company
		 1. Rent a car
		 3. Exit
		Available cars = ''',stock)
		choice=int(input('Enter your choice:'))
		if choice==1:
			print("PRICE OF 1 CAR @RS.500/DAY")
			confrmatn = input("DO YOU WANT TO CONFIRM CAR BOOKING(y/n): ")
			if confrmatn == "y":
				qnt = int(input("ENTER THE NUMBER OF CARS FOR RENT: "))
				if qnt<=stock:
					days = int(input("FOR HOW MANY DAYS DO YOU NEED CAR: "))
					name = input("ENTER YOUR NAME: ")
					cnum = input("ENTER YOUR CONTACT NUMBER: ")
					l.append(name)
					l.append(cnum)
					l.append(qnt)
					l.append(days)
					amut=days*qnt*(500)
					l.append(amut)
					print(amut)
					database[userid]=l
					print(database)
					# Cid = input("ENTER YOUR ID: ")
					bill_gen(name,cnum,userid,qnt,days,amut)
					userid=int(0)

				elif qnt>stock:
					print("SORRY!",qnt,"CARS ARE'NT AVAILABLE AT THIS MOMENT")
			if confrmatn=="n":
				print('ok BYE,,,,')

		if choice==3:
			Print("Thanks for visit:: Exit")

	if userid in database:
		print("""
			What service Do you want ?
			1. Deopsit
			2. Rent more cars
			3. Exit
		 """)
		choice== int(input("Enter choice number:"))
		if choice == 1:
			depo_qnt=int(input('How much cars do you want to Deopsit '))
			if depo_qnt<=database[userid][qnt] and depo_qnt>0:
				qnt=database[userid][qnt]- depo_qnt
			else:
				print("Car deposit qnty is Not acceptable")
