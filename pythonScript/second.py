user_nr_init = input("Insert yout numbers with , : ")
user_nr = user_nr_init.split(",")


for number in user_nr:
	user_nr.append(int(number))


print(user_nr)