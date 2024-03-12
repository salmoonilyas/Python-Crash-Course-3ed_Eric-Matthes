buffet_tuple=("Pizza","Hamburger","French Fries","Fried Chicken","Cheeseburger")
for food in buffet_tuple:
    print(food)

#buffet_tuple[0]="Turkish kebab" #TypeError: 'tuple' object does not support item assignment
buffet_tuple=("Pizza","Turkish kebab","French Fries","Sushi","Cheeseburger")
print("\nRevised Menu:")
for food in buffet_tuple:
    print(food)