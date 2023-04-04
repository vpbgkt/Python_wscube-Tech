email=input('''
	Email format: username@company.com
	Enter your email: ''')
# email='vpbgkt123gsm@.com'
i=0
if '@' in email and '.' in email:
	for i in range (i,len(email)):
		if email[i]=='@':
			break
	username=email[0:i]
	print(username)
	company_name=i+1
	for i in range (i,len(email)):
		if email[i]=='.':
			break
	company_name=email[company_name:i]
	domain=i+1
	domtemp= len(email)-domain
	if email[0]!='@' and company_name.isalnum()==True and (domtemp<=3 and domtemp!=0)  and ' ' not in email:
		domain=email[domain:len(email)]
		print()
		print('Your email :',email,'Accepted')
	else:
		print()
		print('Invalid format used Check again ',email)
else:
	print('Email entred in incorrect format Check for missing @ and . ')