"""
Project: Domino Trainer
Name(s): Jared Kosanovic, Julian Kosanovic
Date: 12/25/2018
Version: 1
Notes: enter_hand() function for project

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
		domino = [domino.split(',')]
		print(domino) #test
		for i in range(0,2):
			if check_int(domino[i]) == False: #If input is not an integer, error
				print("You must enter only integers representing the dots on the domino. Try again.")
				error_flag == True
				break #for loop, not while loop
			else:
				domino[i] = int(i)
				print("int")
				print(domino[i])
		#
		for i in range(0,2): #check for value < 0
			if error_flag == True:
				break #for loop
			elif domino[i] < 0: #Value <0 returns error	
				print("Value must be greater than or equal to 0. Try again.")
				error_flag == True
				break
		if error_flag == False:	
			domino_list.append(domino)
		#print(domino) #test
	#print(domino_list) #test
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