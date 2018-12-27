import pprint

def calculate_routes(route, remaining_hand):
    last_number = route[-1][1]
    route_terminated = True
    for index, domino in enumerate(remaining_hand):
        if last_number in domino:
            route_terminated = False
            remaining_hand_copy = remaining_hand.copy()
            del remaining_hand_copy[index]
            domino_copy = domino.copy()
            if domino_copy[1] == last_number:
                domino_copy.reverse()
            route_copy = route.copy()
            route_copy.append(domino_copy)
            calculate_routes(route_copy, remaining_hand_copy)
    if route_terminated:
        options.append(route.copy())

options = []
hand = [[3,12],[3,4],[3,10],[10,5],[5,0],[12,10],[12,11]]
calculate_routes([[3,3]], hand)
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(options)
