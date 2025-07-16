from random import*
import string
password=""
fun_lst=[]
def capital():
	global password;password+=choice(string.ascii_uppercase)
def small():
	global password;password+=choice(string.ascii_lowercase)
def number_fun():
	global password;password+=str(randint(0,9))
def symbol():
	global password;password+=choice(string.punctuation)
print('#'+'-'*20+"Password Generator"+'-'*20+'#')
try:
	pass_length=int(input("\nPassword length: "))
	if pass_length<4:
		raise Exception("Password length is too small.\nMinimum length is 4.")
	if pass_length>50:
		raise Exception("Password length is too high.\nMaximum length is 50.")
except Exception as error:
	print(f"Error: {error}")
	exit()
print("\nYes type [Y/y] or No type [N/n].")
capital_alpha=input("\nCapital alphapet: ").upper()
if capital_alpha=='Y':fun_lst.append(capital)
small_alpha=input("\nSmall alphapet: ").upper()
if small_alpha=='Y':fun_lst.append(small)
number=input("\nNumbers: ").upper()
if number=='Y':fun_lst.append(number_fun)
special_char=input("\nSpecial charater: ").upper()
if special_char=='Y':fun_lst.append(symbol)
for i in range(pass_length):
		shuffle(fun_lst)
		for fun in fun_lst:
			fun()
			if len(password)==pass_length:
				print(f"\nYour Password: {password}")
				exit()
