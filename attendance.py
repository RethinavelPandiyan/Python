def cal_att(total_days=0,absent_days=0):
	if total_days==0:
		return 0
	return round(((total_days-absent_days)/total_days)*100,2)
total_days=float(input("Enter total days: "))
absent_days=float(input("Enter absent days: "))
if absent_days>total_days:
	print("Your absent days are more than working days.")
else:
	print(f"Total days you attended: {total_days-absent_days}")
	print(f"Your attendance percentage: {cal_att(total_days,absent_days)}%")