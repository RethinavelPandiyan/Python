m_name=input("Enter name: ").lower()
f_name=input("Enter names to check: ").split(",")
set_name=[]
non_set_name=[]
for i in f_name:
	count=0
	for j in i.lower():
		if j in m_name:
			count+=1
	if count==len(i):
		set_name.append(i)
	else:
		non_set_name.append(i)
set_name=list(set(set_name))
non_set_name=list(set(non_set_name))
non_set_name.sort()
set_name.sort()
if len(set_name)!=0:
	print("\nSet names:")
	for i in set_name:
		print(i.title())
	print("\nTotal set names:",len(set_name))
else:
	print("\nSet names are Zero.")
if len(non_set_name)!=0:
	print("\nNon set names:")
	for i in non_set_name:
		print(i.title())
	print("\nTotal non set names:",len(non_set_name))
else:
	print("\nNon set names are Zero.")