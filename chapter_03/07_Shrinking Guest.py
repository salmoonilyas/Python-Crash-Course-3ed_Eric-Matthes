persons=["Adam","Jane","David"]

print(f"{persons[0]}, could not make it to the dinner today at 20:00.")
persons[0]="Jenny"

print(f"{persons[0]}, let's have dinner today at 20:00.")
print(f"{persons[1]}, let's have dinner today at 20:00.")
print(f"{persons[2]}, let's have dinner today at 20:00.")


print(f"{persons[0]}, I have found a bigger table for dinner.")
print(f"{persons[1]}, I have found a bigger table for dinner.")
print(f"{persons[2]}, I have found a bigger table for dinner.")

persons.insert(0,'Trump')
persons.insert(2,"Biden")
persons.append("Johnson")

print(f"{persons[0]}, let's have dinner today at 20:00.")
print(f"{persons[1]}, let's have dinner today at 20:00.")
print(f"{persons[2]}, let's have dinner today at 20:00.")
print(f"{persons[3]}, let's have dinner today at 20:00.")
print(f"{persons[4]}, let's have dinner today at 20:00.")
print(f"{persons[5]}, let's have dinner today at 20:00.")

print("You can invite only two people for dinner.")

print(f"{persons.pop()}, I are sorry I can't invite you to dinner.")
print(f"{persons.pop()}, I are sorry I can't invite you to dinner.")
print(f"{persons.pop()}, I are sorry I can't invite you to dinner.")
print(f"{persons.pop()}, I are sorry I can't invite you to dinner.")

print(f"{persons[0]}, you are invited to dinner today at 20:00.")
print(f"{persons[1]}, you are invited to dinner today at 20:00.")

del persons[0]
del persons[0]
print(persons)