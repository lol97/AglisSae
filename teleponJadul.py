input_str = input("masukkan pad : ")
db_key = {2:"a",22:"b",222:"c"
}
for x in input_str.split(" "):
	try:
		print(db_key[int(x)],end="")
	except Exception as e:
		pass
print()