"""
Project: Domino Trainer
Name(s): Jared Kosanovic, Julian Kosanovic
Date: 12/25/2018
Version: ??
Notes: enter_hand() function for project
Doesn't currently work
"""
#
def check_int(x): 
	try:
		int(x)
		return True
	except ValueError:
		return False 

#
def enter_hand():
	domino_list = []
	print("Please enter the two groups of numbers on a domino separated by a comma,", #Enter domino separated by comma
		"then press return to enter the next domino until complete: ") #Enter nothing to finish
	while True:
		error_flag = False
		domino = input()
		if domino == '': #Enter nothing to finish
			break
		#domino=[int(num) for num in domino.split(',')]
		#
		domino = domino.split(',')
		print(domino) #test
		for i in domino:
			#print(i) #test
			if check_int(i) == False: #If input is not an integer, error
				print("You must enter only integers representing the dots on the domino. Try again.")
				error_flag = True
				break #for loop, not while loop
			else:
				i = int(i)
				#print("int") #test
				#print(i) #test
				if i < 0: #Value <0 returns error	
					print("Value must be greater than or equal to 0. Try again.")
					error_flag = True
					break
		if error_flag == False:	
			domino=[int(num) for num in domino]
			print("current domino", domino) #test
		if domino_list != None: #run if domino_list is not empty to check for duplicates
			test = []
			test = domino
			test.reverse()
			for j in domino_list:
				print("j", j) #test last
				print("test", test) #test
				#print("reverse test", test.reverse()) #test
				if j == domino or j == test: #if duplicate
					print("That domino is already in the list. Try again.")
					error_flag = True
		if error_flag == False: #Everything is fine, put the domino in the list
			print(domino, "added to list")
			domino_list.append(domino)
		#print(domino) #test
	print("domino list", domino_list) #test
	#Check each domino input 
	#Check for duplicate dominoes in the hand
	#Return array of dominos
	
enter_hand()

""" Code graveyard that may be useful somewhere else

for i in range(0,len(domino_list)):
		for j in range(0,2):
			#print(domino_list[i][j])#test
			if domino_list[i][j] < 0:
	
"""