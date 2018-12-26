def calculate_best_path():
    options = []
    for domino in hand:
        print("domino: " + str(domino))
        if start_number in domino:
            print("start_number found in domino")
            #remaining_hand = hand
            #remaining_hand.remove(domino)
            #print("remaining hand: " + str(remaining_hand))
            #options.append([[domino],remaining_hand])
            options.append(domino)

    
    print(options)

start_number = 3
hand = [[3,10],[3,4],[10,5],[5,0],[10,12],[12,11]]
calculate_best_path()
