def traffic_light(color):
    match color:
        case "red":
            print("Stop")
        case "green":
            print("Go")
        case "yellow":
            print("Wait")


while True:
    try:
        color = input("Enter a color: ").strip().lower()
        if color != "red" and color != "green" and color != "yellow":
            raise ValueError("it is not a valid color should be red, green or yellow")

        traffic_light(color)

    except ValueError as e:
        print(f"Error: {e}")

