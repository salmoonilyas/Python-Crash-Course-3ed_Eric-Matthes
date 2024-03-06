places=["Lapland", "Barcelona","Hallstatt","Saturnia","Provence"]
print("Original list: ",places)

print("Sorted list without changing original list: ",sorted(places))
print("Original list: ",places)

print("Reverse sorted list without changing original list: ",sorted(places,reverse=True))
print("Original list: ",places)

places.reverse()
print("Reversed the original list: ",places)

places.reverse()
print("Back to Original list by reversing second time: ",places)

places.sort()
print("Sorted original list: ",places)

places.reverse()
print("Reverse sorted original list: ",places)
