def flame(name_1,name_2):
	name_1=name_1.lower()
	name_2=name_2.lower()
	for letter in name_1:
		if letter in name_2:
			name_1=name_1.replace(letter,"",1)
			name_2=name_2.replace(letter,"",1)
	relation=["Friend","Love","Affection","Marriage","Enemie","Sister"]
	return(relation[((len(name_1)+len(name_2)-1)%len(relation))])