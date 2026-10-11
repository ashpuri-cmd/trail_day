import trail
from trail import route as rt
from trail import weather
from trail import snacks as food
from trail.camp import pitch

def main():
    print("Pack:", trail.gear.pack_weight(3), "lb")
    print("Route:", rt.describe())
    print("Sky:", weather.forecast())
    print("Snack:", food.pick())
    print(pitch("Ridge"))


if __name__ == "__main__":
    main()
