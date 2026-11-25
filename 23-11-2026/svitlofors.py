def traffic_light_if(color: str):
    if color == "red":
        print("Stop")
    elif color == "green":
        print("Go")
    elif color == "yellow":
        print("Wait")
    else:
        print("unknown color")

def traffic_light_match(color: str):
    match color:
        case "red":
            print("Stop")
        case "green":
            print("Go")
        case "yellow":
            print("Wait")
        case _:
            print("unknown color")

color = input("Enter traffic light color (red, green, yellow): ").strip().lower()

print("Варіант if/elif/else:")
traffic_light_if(color)

print("Варіант match/case:")
traffic_light_match(color)

