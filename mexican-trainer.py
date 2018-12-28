import pprint

# Resursively calculates all possible routes given a hand and a starting
# domino.
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
        routes.append(route.copy())

# Returns a dict of domino routes, where the key is a count of the dots in the
# route.
def get_scored_routes():
    scored_routes = {}

    for route in routes:
        score = 0
        for domino in route:
            for number in domino:
                score += number

        if score in scored_routes:
            existing_route = scored_routes[score]
            existing_route_length = len(existing_route)
            current_route_length = len(route)

            if existing_route_length < current_route_length:
                # Favor the route with more dominos if the score is equal
                scored_routes[score] = route
            elif existing_route_length == current_route_length:
                # If the amount of dominos and dots in the routes are equal,
                # favor the route with the most doubles.
                existing_route_doubles = count_doubles(existing_route)
                current_route_doubles = count_doubles(route)
                if existing_route_doubles < current_route_doubles:
                    scored_routes[score] = route
        else:
            scored_routes[score] = route

    return scored_routes

# Returns the number of dominos in a route that are doubles
def count_doubles(route):
    return len([domino for domino in route if domino[0] == domino[1]])

def the_whole_domino_set():
    dominos = []
    for left_num in range(13):
        for right_num in range(13):
            dominos.append([left_num, right_num])

    print("all dominos: " + str(dominos))
    return dominos

routes = []
hand = [[3,12],[3,4],[3,10],[10,5],[5,0],[4,10],[10,11],[12,10],[12,11],[12,12],[4,9],[9,5],[12,3],[11,6],[11,5],[4,7]]

calculate_routes([[3,3]], hand)
#calculate_routes([[3,3]], the_whole_domino_set())
print("all possible routes")
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(routes)

print("number of possible routes: " + str(len(routes)))

scored_routes = get_scored_routes()
print("scored routes")
pp.pprint(scored_routes)

print("The best route:")
pp.pprint(scored_routes[max(scored_routes, key=int)])
