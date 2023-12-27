foods = []
prices = []
total = 0
while True:
    while True:
        food = input("Enter a food to buy ('q' to Quit): ")
        if food.isalpha():
            break
        else:
            print("Invalid input.")

    if food.lower() == 'q':
        break
    else:
        while True:
            try:
                price = float(input(f"Enter the price of a {food}: $"))
                break
            except ValueError:
                print("Invalid input")
        prices.append(price)
        foods.append(food)

print("-----YOUR CART-----")
for food in foods:
    print(food, end=" ")

for price in prices:
    total += price
print(f"Your total bill: ${total}")

