import sqlite3
conn=sqlite3.connect("Vishal Ki School.db")
cur=conn.cursor()

# data ="""
# CREATE TABLE student_info(
# 	name char(50),
# 	fname char(50),
# 	eng int,
# 	maths int,
# 	sci int)
# 	"""
# cur.execute(data)

# conn.commit()

conn.close()
# data=""""
# 	INSERT IN student_info values
# """
main_data = {'a': ['ab', 10, 10, 10], 'b': ['bb', 20, 20, 20], 'c': ['cc', 50, 50, 50]}
def data_entry(name,fname):
				eng  = int(input("enter your eng out of 100 : "))
				if eng <=100:
					maths  = int(input("enter your maths out of 100 : "))
					if maths <=100 : 
						sci = int(input("enter your sci out of 100 : "))
						if sci <=100 : 
								l.append(fname)
								l.append(eng)
								l.append(maths)
								l.append(sci)
								main_data[name]=l 
						else :
							print("wrong entry")
					else : 
						print("wrong entry")
				else : 
					print("wrong entry : ")



def data_show():
			li = main_data[name_1]  # [fname,eng,maths,sci]
			print("eng : ",li[1])
			print("maths : ",li[2])
			print("sci  : ",li[3])
			total = li[1]+li[2]+li[3]
			per = total/3
			print("total : ",total)
			print("per : ",per)
			if per>=60:
				print("1st div")
			elif per>=50:
				print("2nd div")
			elif per >=36:
				print("3rd div")
			else :
				print("fail")

print("Wscube E School")
while True:
	var = input("""
	1. Data Entry 
	2. Data Show 
	3. per 
	4. Exit   : """)
	if var == "1":
		no = int(input("enter no data entry : "))
		for i in range(no):
			l = []
			name = input("enter your name : ")
			fname = input("entry your famne : ")
			if name not in main_data:
				data_entry(name,fname)
				
			elif fname not in main_data[name]:
				data_entry(name+fname,fname)
			else :
				print("already e : ")
			print()

	elif var == "2":
		name_1 = input("enter your name : ")
		if name_1 in main_data:
			data_show()
		else :
			print("st not in school")
	elif var == "3":
		code  = input("enter your code : ")
		if code =="p1234":
					name_1 = input("enter your name : ")
					if name_1 in main_data:
						print("fname : ",fname)
						data_show() #====================
					else :
						print("st not in school")
		else :
			print("wrong code : ")
	elif var == "4":
		print("Thank you : ")
		break
	else :
		print("wrong input :")
	print()
	print(main_data)


