"""
Project: Domino Trainer
Name(s): Jared Kosanovic, Julian Kosanovic
Date: 12/25/2018
Version: Final
Notes: enter_hand() function for project

"""

def check_int(x): 
	try:
		int(x)
		return True
	except ValueError:
		return False 

def enter_hand():
	domino_list = []
	print("Please enter the two groups of numbers on a domino separated by a comma,", #Enter domino separated by comma
		"then press return to enter the next domino until complete: ") #Enter nothing to finish
	while True:
		error_flag = False
		domino = input()
		if domino == '': #Enter nothing to finish
			break
		domino = domino.split(',')
		for i in domino:
			if check_int(i) == False: #If input is not an integer, error
				print("You must enter only integers representing the dots on the domino. Try again.")
				error_flag = True
				break #for loop, not while loop
			else:
				i = int(i)
				if i < 0: #Value <0 returns error	
					print("Value must be greater than or equal to 0. Try again.")
					error_flag = True
					break
		if error_flag == False:	
			domino=[int(num) for num in domino]
		if domino_list != []: #run if domino_list is not empty to check for duplicates
			for j in domino_list:
				if j == domino: #if duplicate
					print("That domino is already in the list. Try again.")
					error_flag = True
					break
				domino.reverse() #reverse and check
				if j == domino: #if duplicate
					print("That domino is already in the list. Try again.")
					error_flag = True
					break
				else:
					domino.reverse() #back to normal
		if error_flag == False: #Everything is fine, put the domino in the list
			print(domino, "added to list")
			domino_list.append(domino)
	print("Here is the final list of dominos you entered:", domino_list) #test
	return domino_list #Return array of dominos