#  Last sanity check: 2020-04-29
user_nr_init = input("Insert yout numbers with , : ")
user_nr = user_nr_init.split(",")


for number in user_nr:
	user_nr.append(int(number))


print(user_nr)