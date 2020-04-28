#  Last sanity check: 2020-04-28
import random

def askAndCheck():
	user = input("Baga un nr. intre 0 si 9: ")
	if int(user) in magic:
		return "BRAVO! AI GHICIT!" 
	else:	
		return "NU AI NIMERIT!" 


magic = [random.randint(0, 9)]


def runXtimes(ch): 
	for i in range(ch): 	
		print("Incercari ramase: {}".format(ch-i))
		print(askAndCheck())
		

ch = int(input("Numar incercari: "))
runXtimes(ch)


print("Numarul era: {}".format(magic))
