import pprint

def calculate_routes(route, remaining_hand):
    last_number = route[-1][1]
    for domino in remaining_hand:
        if last_number in domino:
            remaining_hand.remove(domino)

            if domino[1] == last_number:
                domino.reverse()

            route.append(domino)
            calculate_routes(route, remaining_hand)
        else:
            options.append(route)

options = []
start_number = 3
hand = [[3,10],[3,4],[10,5],[5,0],[10,12],[12,11]]
calculate_routes([[3,3]], hand)
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(options)
