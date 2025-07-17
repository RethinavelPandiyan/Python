from random import randint,choice,shuffle
import string
class PasswordGenerator:
	def __init__(self):
		self.password=""
		self.fun_lst=[]
	def capital(self):
		return(choice(string.ascii_uppercase))
	def small(self):
		return(choice(string.ascii_lowercase))
	def number_fun(self):
		return(str(randint(0,9)))
	def symbol(self):
		return(choice(string.punctuation))
	def start(self):
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
		capital_alpha=input("\nCapital alphapet? ").upper()
		if capital_alpha=='Y':self.fun_lst.append(self.capital)
		small_alpha=input("\nSmall alphapet? ").upper()
		if small_alpha=='Y':self.fun_lst.append(self.small)
		number=input("\nNumbers? ").upper()
		if number=='Y':self.fun_lst.append(self.number_fun)
		special_char=input("\nSpecial charater? ").upper()
		if special_char=='Y':self.fun_lst.append(self.symbol)
		for i in range(pass_length):
				shuffle(self.fun_lst)
				for fun in self.fun_lst:
					self.password+=fun()
					if len(self.password)==pass_length:
						print(f"\nYour Password: {self.password}")
						exit()
if __name__=="__main__":
	pg=PasswordGenerator()
	pg.start()
	
