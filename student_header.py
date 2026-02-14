import student_database
def demo_use():
	student_database.print_data("Welcome to student data management system. This application can make you to manage the students data easily and effectively with multiple functions.\nThis will allow you to create a new student data, edit the existed data, remove the data, search the data, and show the all data in one click.\nThis will maintain the different theme for every time you use the application.\nSupport:\nEmail:rethinavelpandiyan702@gmail.com\nWhatsapp:+91 9791954029\nType '--help' for to find the step to use the application.\n")
def help_page():
	student_database.print_data("1.Add Student: For create the new student details(Name, Age, Gender, Roll No).\n")
	student_database.print_data("2.Remove Student: For delete the selected student entire data, student are selected by Roll No.\n")
	student_database.print_data("3.Edit Student Data: For edit the already existed student data by using Roll No.\n")
	student_database.print_data("4.Show all data: For get the all students data.\n")
	student_database.print_data("5.Search Student: For find the specific student data by Roll No.\n")
	student_database.print_data("6.Exit: For stop the application and saved the students data on device.\n")