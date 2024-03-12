car= "Subaru"
print("is car == 'Subaru'? I predict True.")
print(car == "Subaru")

print("\nIs car!= 'Subaru'? I predict False.")
print(car != 'Subaru')


car= "Volkswagen"
print("\nis car == 'volkswagen'? I predict True.")
print(car.lower() == "volkswagen")

print("\nis car == 'Subaru'? I predict False.")
print(car.lower() == "Subaru")

car= "BMW"
print("\nis car >= 'Volkswagen'? I predict False.")
print(car >= "Volkswagen")

print("is car <= 'Toyota'? I predict True.")
print(car <= "Toyota")

print("is car == 'Ford' or car == 'BMW'? I predict True.")
print(car == "Ford" or car == "BMW")

print("is car == 'Ford' or car == 'BMW'? I predict False.")
print(car == "Ford" or car == "Honda")

print("is car == 'Ford' or car == 'BMW'? I predict True.")
print(car == "BMW" and car == "BMW")

print("is car == 'Ford' or car == 'BMW'? I predict False.")
print(car == "Ford" and car == "Honda")

cars=["Volkswagen","Honda","BMW"]
print("is SIAC in list of cars'? I predict False.")
print("SIAC" in cars)

print("is SIAC not in list of cars'? I predict True.")
print("SIAC" not in cars)
