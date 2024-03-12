my_pizzas=["Classic Margherita","Spicy Pepperoni","BBQ Chicken","Margherita"]
friends_pizzas=my_pizzas[:]

my_pizzas.append("New Yorker")
friends_pizzas.append("Chicken Fajita")

print("My favorite pizzas are:")
for pizzas in my_pizzas:
    print(pizzas)

print("\nMy friend's favorite pizzas are:")
for pizzas in friends_pizzas:
    print(pizzas)