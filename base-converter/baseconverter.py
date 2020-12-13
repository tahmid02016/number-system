num, base = input().split()
if (num[0] == "-"):
	print("Error: this programme only supports positive numbers.")
	exit()

D = int(num, int(base))
B = bin(D)[2:]
O = oct(D)[2:]
H = hex(D)[2:]

L = len(B)
if L < 6:
	L = 6
	B += " "*(L-len(B))

D = str(D)
D += " "*(L-len(D))
O += " "*(L-len(O))
H += " "*(L-len(H))

line1 = "+-------------+";
line2 = ''.join(["-" for i in range(L+2)])
line3 = ''.join((line1, line2, "+"))
print(line3)
print("| {} | {} |". format("Decimal    ", D))
print(line3)
print("| {} | {} |". format("Binary     ", B))
print(line3)
print("| {} | {} |". format("Octal      ", O))
print(line3)
print("| {} | {} |". format("Hexadecimal", H))
print(line3)
