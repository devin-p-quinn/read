import datetime

# a simple program to tell you how many pages to read each day
start_day_month = int(input("Month you want to start reading "))
start_day = int(input("Day you want to start "))

current_day = datetime.date(2021, start_day_month, start_day)

while True:
	book_name = input("What is the name of your book? ")
	length_book = int(input("How long is the book you want to read? "))
	pages_day = int(input("How many pages do you want to read per day? "))
	current_page = int(input("What page are you starting on? "))


	pages_to_go = length_book - current_page

	days = pages_to_go // pages_day

	print(f"{book_name} is {length_book} pages long")
	print(f"You want to read {pages_day} pages per day")

	print(f"It will take you {days} days to read {book_name}")



	while days > 0:
		days -= 1
		current_page += pages_day
		print(f"On {current_day} read to page {current_page}")
		current_day += datetime.timedelta(days=1)

	decision = input("Do you want to add another book (y/n)")

	if decision == "y":
		continue
	else:
		break
