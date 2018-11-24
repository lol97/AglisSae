condition = True
ke = 1
while(condition):
	cmd = input("enter word : ").upper()
	if(cmd == "HAI"):
		print("case ", ke, " : INDONESIA")
	elif(cmd == "DAMANG"):
		print("case ", ke, " : SUNDA")
	elif(cmd=="REANG"):
		print("case ",ke," : CIREBON")
	elif(cmd == "#"):
		break
	else:
		print("case ",ke," : UNKNOWn")