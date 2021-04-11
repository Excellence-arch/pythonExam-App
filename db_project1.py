import mysql.connector

mycon = mysql.connector.connect(host="localhost", user="root", passwd="", database="student_db")

mycursor = mycon.cursor()
# mycursor.execute("create database student_db")
# mycursor.execute("show databases")
# for k in mycursor:
# 	print(k)

# mycursor.execute("create table students(students_id INT(4), Fullname VARCHAR(30), Class VARCHAR(20), address VARCHAR(20))")
# mycursor.execute("alter table students add unique(Fullname;")
# mycursor.execute("alter table students add unique(Fullname)")


def main():
	l = ["1. Register", "2. Start Exam"]
	for i in l:
		print(i)
	p = input("Your choice > ")
	if p == "1":
		reg()
	elif p == "2":
		game()

def game():
	name = input("Enter your name > ")
	query = "SELECT * FROM students WHERE Fullname=%s"
	value = (name,)
	mycursor.execute(query, value)
	myreg = mycursor.fetchall()
	if myreg:
		print(name, "You can start your exam...")
		nt = 0
		score = 0
		questions = ["What is 5+5", "Extraction of aluminium from its ore is by?",
					 "Which of the following colours is imparted by Calcium ion into a flame?",
					 "In which of the following processes does coal give coal gas, coal tar, ammoniacal liquor and coke?"]
		options = [["a.10", "b.15", "c.5", "d.55"],
				   ["a.floatation", "b.electrolysis", "c.roasting", "d.reduction with coke"],
				   ["a.lilac", "b.yellow", "c.blue", "d.brick red"],
				   ["a.liquefaction", "b.steam distillation", "c.destructive distillation", "d.hydrolysis"]]
		answers = ["a", "b", "d", "c"]
		for que in questions:
			print(que)
			print(options[nt])
			ans = input("Your answer > ")

	else:
		print("Wrong name")
		game()

def reg():
	n = int(input("How many students do you want to register > "))
	for k in range(n):
		fulname = input("Enter your full name > ")
		clas = input("What class are you > ")
		adres = input("Where do you leave > ")
		myquery = "INSERT INTO students(Fullname, Class, address) VALUES(%s, %s, %s)"
		val = (fulname, clas, adres)
		mycursor.execute(myquery, val)
		mycon.commit()

main()


