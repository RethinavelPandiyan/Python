import json
import time
import os
from pathlib import Path
import student_header
from random import randint
color=randint(90,97)
def app_reset():
	file=Path("data.json")
	file.unlink(missing_ok=True)
	print_data("Do you want to Reset ths app [Y/N]:")
	choice=input().strip()
	if choice.upper()=="Y":
		gen_number=randint(1000,10000)
		print_data(str(gen_number))
		print_data("\nEnter the 4 digit number:")
		user_number=int(input().strip())
		if user_number==gen_number:
			print_data("\nReset the application successfully.")
		else:
			print_data("\nWrong number.\n")
	else:
		print_data("Operation cancelled.")
	exit(1)
def init():
	try:
		file=open("data.json","r")
		file.close()
	except Exception:
		student_header.demo_use()
		file=open("data.json","w")
		data={}
		json.dump(data,file)
		file.close()
def print_data(data):
		for i in data:
			print(i,flush=True,end="")
			time.sleep(1/100)
def add_student():
	print_data("\nAdd Student\n")
	value=0
	try:
		file=open("data.json","r")
	except Exception as e:
		length=0
		data={}
		value=1
	if value!=1:
		data=json.load(file)
		length=len(data)
		file.close()
	try:
		print_data("Enter Name:")
		name=input().strip()
		print_data("Enter Age:")
		age=int(input().strip())
		print_data("Enter Gender:")
		gender=input().strip()
		print_data("Enter Roll No:")
		roll_num=input().strip()
		roll_num=roll_num.upper()
		for i in data.values():
			if i["Roll_Number"]==roll_num:
				print_data(roll_num+" is already use for "+i["Name"]+".Try other Roll No.\n")
				return 0
	except Exception as e:
		print_data(f"\033[91m{e}\033[0m")
		exit(1)
	new_data={length+1:{"Name":name,"Age":age,"Gender":gender,"Roll_Number":roll_num}}
	data.update(new_data)
	try:
		file=open("data.json","w")
	except Exception as e:
		print_data(f"\033[91m{e}\033[0m")
		exit(1)
	json.dump(data,file)
	file.close()
	print_data("\033[92mAdded Successfully\033[0m\n")
def show_all_data():
	print_data('\nAll Data\n')
	try:
		file=open("data.json","r")
	except Exception as e:
		print_data(f"\033[31mData not found.\033[0m")
		exit(1)
	data=json.load(file)
	female=0
	male=0
	others=0
	for i in data.values():
		print_data("\033["+str(color)+"m"+"_"*20+"\033[0m\n")
		print_data("Name:"+i["Name"]+"\n")
		print_data("Age:"+str(i["Age"])+"\n")
		print_data("Roll No:"+i["Roll_Number"]+"\n")
		print_data("Gender:"+i["Gender"]+"\n")
		if i["Gender"].title()=="Female":
			female+=1
		elif i["Gender"].title()=="Male":
			male+=1
		else:
			others+=1
	print_data("\033["+str(color)+"m"+"_"*20+"\033[0m\n")
	print_data("Females:"+str(female)+"\n")
	print_data("Males:"+str(male)+"\n")
	print_data("Others:"+str(others)+"\n")
	print_data("Total:"+str(female+male+others)+"\n")
	file.close()
def edit_student_data():
	print_data("\nStudent Data Edit\n")
	roll_num=input("Enter Roll No:").strip()
	try:
		file=open("data.json","r")
	except Exception as e:
		print_data(f"\033[91m{e}\033[0m")
		exit(1)
	data=json.load(file)
	found=False
	for i in data.values():
		if i["Roll_Number"]==roll_num.upper():
			print_data("Name:"+i["Name"]+"\n")
			print_data("Age:"+str(i["Age"])+"\n")
			print_data("Roll No:"+i["Roll_Number"]+"\n")
			print_data("Gender:"+i["Gender"]+"\n")
			print_data("Edit Page\n")
			name=input("Enter Name:").strip()
			age=int(input("Enter Age:").strip())
			gender=input("Enter Gender:").strip()
			i["Name"]=name
			i["Age"]=age
			i["Roll_Number"]=i["Roll_Number"]
			i["Gender"]=gender
			found=True
	file.close()
	try:
		file=open("data.json","w")
	except Exception as e:
		print_data(f"\033[91m{e}\033[0m")
		exit(1)
	json.dump(data,file)
	if found:
		print_data("\033[092mUpdated Successfully\033[0m\n")
	else:
		print_data("\033[091mRoll No does't exists\033[0m\n")
def remove_student():
	print_data("Remove Student\n")
	roll_num=input("Enter Roll No:").strip()
	try:
		file=open("data.json","r")
	except Exception as e:
		print_data(f"\033[91m{e}\033[0m")
		exit(1)
	data=json.load(file)
	file.close()
	value=0
	for i,j in data.items():
		if j["Roll_Number"]==roll_num.upper():
			value=i
	if value!=0:
		del data[value]
		print_data("\033[92mRemoved Successfully\033[0m\n")
	else:
		print_data(f"\033[91m{roll_num} does't exists.\033[0m\n")
	try:
		file=open("data.json","w")
	except Exception as e:
		print_data(f"\033[91m{e}\033[0m")
		exit(1)
	json.dump(data,file)
	file.close()
def search_student():
	print_data("\nSearch Student\n")
	print_data("\033["+str(color)+"m"+"_"*20+"\033[0m\n")
	print_data("Enter Roll No:")
	roll_num=input().strip()
	try:
		file=open("data.json","r")
	except Exception as e:
		print_data(f"\033[91m{e}\033[0m")
		exit(1)
	data=json.load(file)
	found=0
	for i in data.values():
		if i["Roll_Number"]==roll_num.upper():
			print_data("Found:\n")
			print_data("Name:"+i["Name"]+"\n")
			print_data("Age:"+str(i["Age"])+"\n")
			print_data("Roll No:"+i["Roll_Number"]+"\n")
			print_data("Gender:"+i["Gender"]+"\n")
			found+=1
	if found==0:
		print_data("\033[091mStudent not found at "+roll_num.upper()+"\033[0m\n")
	file.close()
def main():
	while True:
		print_data("\033["+str(color)+"m"+"_"*20+"\033[0m\n")
		print_data("1.Add Student\n")
		print_data("2.Remove Student\n")
		print_data("3.Edit Student Data\n")
		print_data("4.Show All Data\n")
		print_data("5.Search Student\n")
		print_data("6.Reset\n")
		print_data("7.Exit\n")
		try:
			choice=input("Enter option:").strip()
		except Exception:
			print_data(f"\033[91mYou press ENTER/RETURN key without type value..\033[0m")
			exit(1)
		if choice=="1":
			add_student()
		elif choice=="2":
			remove_student()
		elif choice=="3":
			edit_student_data()
		elif choice=="4":
			show_all_data()
		elif choice=="5":
			search_student()
		elif choice=="6":
			app_reset()
		elif choice=="7":
			print_data("Thank You :)")
			exit(0)
		elif choice=="--help":
			student_header.help_page()
		elif choice=="clear":
			os.system("cls" if os.name=='nt' else "clear")
		else:
			print_data("Invalid Option (:\n")
if __name__=="__main__":
	init()
	main()