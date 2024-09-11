"""Practice with conditionals and elif"""


def get_weather_report() -> str:
    """Takes type of weather as input and returns advice"""
    weather: str = input("What is the weather?")
    if weather == ("rainy" or "cold"):
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize this weather.")
    return weather


get_weather_report()
