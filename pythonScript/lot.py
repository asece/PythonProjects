#  Last sanity check: 2020-04-28
import random
print("WELCOME TO THE LOTTERY APP!")
def menu():
	user_numbers = get_numbers()

	lottery_numbers = create_lottery_numbers()
	
	matched_numbers = user_numbers.intersection(lottery_numbers)
	print("You matched: {}. You won ${}.".format(matched_numbers, 100**len(matched_numbers)))
	print("Lucky numbers are:"),print(lottery_numbers)
	

#You can pick 6 numbers
def get_numbers():
	number_csv = input ("Enther 6 numbers, separated by , :")
	# Create a set fo int from number_csv 
	number_list = number_csv.split(",")
	integer_set = {int(number) for number in number_list}
	return integer_set

#lottery picks 6 lucky numbers ( 1~20 )
def create_lottery_numbers():
	values = set()	#Can't initialise with {} !!
	while len(values) < 6:
		values.add(random.randint(1,20))
	return values		


menu()
