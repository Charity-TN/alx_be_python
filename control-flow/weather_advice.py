#Program meant to ask user about the weather conditions and advice on the proper clothing
weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()

if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
