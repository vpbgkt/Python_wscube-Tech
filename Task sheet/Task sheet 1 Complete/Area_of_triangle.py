user=input("\n\nDo you want to find area of triangle using height and base only ?\n Enter yes or NO : ")

if user=='yes' or user=='Yes' or user == 'YES':
	base=eval(input("Enter the value of base: "))
	height=eval(input("Enter the value of height : "))	
	area=1/2*(base*height)
	print("The area of tringle is: ",area)

elif user=='no' or user=='No' or user == 'NO':
	
	print("Area for 3 sides: ")
	side1=eval(input("Enter 1st side: "))
	side2=eval(input("Enter 2nd side: "))
	side3=eval(input("Enter 3rd side: "))
	semi_perimeter=(side1+side2+side3)/2
	Area=(semi_perimeter*(semi_perimeter-side1)*(semi_perimeter-side2)*(semi_perimeter-side3))**0.5
	print("Area of tringle with three sides is : ",Area)

else :
	print("\nWrong value Entred. check again")