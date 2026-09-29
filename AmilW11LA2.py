AmilPizza = str(input("Enter pizza flavor (Hawaiian, Beef, or Chicken): "))

AmilSize = str(input("Enter pizza size: "))

if AmilPizza.lower() not in ["hawaiian", "beef", "chicken"] or AmilSize.lower() not in ["small", "medium", "large"]:
    print("Invalid flavor or size. Please try again.")

else:
    AmilPrices = [("Hawaiian", "Small", 350), ("Hawaiian", "Medium", 450), ("Hawaiian", "Large", 550), ("Beef", "Small", 380), ("Beef", "Medium", 480), ("Beef", "Large", 580), ("Chicken", "Small", 410), ("Chicken", "Medium", 510), ("Chicken", "Large", 610)]

    for flavor, size, price in AmilPrices:
        if flavor.lower() == AmilPizza and size.lower() == AmilSize:
            print(f"Order Summary: \n{flavor} pizza \n{size}\nThe price is {price}")
            break