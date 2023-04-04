print("\n------WELCOME TO THE CAR RENTAL COMPANY------")
stock = int(50)
while True:
	print("\n\tAVAILABLE CARS FOR RENT: ",stock)
	print('''
    1.RENT
    2.DEPOSITE
    3.EXIT
    ''')
    id = input("ENTER YOUR ID: ")
    if id== Cid:
	choice = input("PLEASE SELECT YOUR CHOICE: ")
	if choice=='1':
		print("PRICE OF 1 CAR @RS.500/DAY")
		confrmatn = input("DO YOU WANT TO CONFIRM CAR BOOKING(yes/no): ")
		if confrmatn == "yes":
			qnt = int(input("ENTER THE NUMBER OF CARS FOR RENT: "))
			if qnt>stock:
				print("SORRY!",qnt,"CARS ARE'NT AVAILABLE AT THIS MOMENT")
			elif qnt<=0:
				print("INVALID INPUT")
			elif qnt<=stock:
				days = input("FOR HOW MANY DAYS DO YOU NEED CAR: ")
				name = input("ENTER YOUR NAME: ")
				cnum = input("ENTER YOUR CONTACT NUMBER: ")
				Cid = inpur("ENTER YOUR ID: ")


















# import random
# game_data=['stone','paper','scissors']
# bot = random.choice(game_data)
# print(bot)
# user='stone'
# if bot=='stone' and user=='paper':
# 	print('You Won!')
# elif bot=='stone' and user=='scissors':
# 	print('Bot win...')
# elif bot=='paper' and user=='scissors':
# 	print('You won')
# elif bot=='scissors' and  user=='stone':
# 	print('You won!')
# else:
# 	print('Out of range')
