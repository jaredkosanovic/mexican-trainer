"""
Project: Domino Trainer
Name(s): Jared Kosanovic, Julian Kosanovic
Date: 12/25/2018
Version: 1
Notes: enter_hand() function for project

"""

def enter_hand():
	domino_list = []
	print("Please enter the two groups of numbers on a domino separated by a comma,", #Enter domino separated by comma
		"then press return to enter the next domino until complete: ") #Enter nothing to finish
	while True:
		domino = input()
		if domino == '': #Enter nothing to finish
			break
			
		domino_list.append([int(num) for num in domino.split(',')])
		#print(domino) #test
	#print(domino_list) #test
	for i in range(0,len(domino_list)):
		for j in range(0,2):
			#print(domino_list[i][j])#test
			if domino_list[i][j] < 0:
				print("You entered in a value less than zero. Game over") #test
	#Check each domino input 
	#Check for duplicate dominoes in the hand
	#Return array of dominos
	
enter_hand()