countries=["Canada", "France", "Germany", "Italy", "Japan", "United Kingdom", "United States"]

print(countries[0]) #print first item of the list
print(countries[-1]) #print last item of the list

countries[0]="Austria" #replace item at index position 0
countries.insert(1,"Canada") #add item to index position 1
countries.append("Belgium") #append item

print(sorted(countries)) #Sorted without changing original list
print(sorted(countries,reverse=True)) #Reverse sorted without changing original list

del countries[0] #Austria Deleted

popItem=[]
popItem.append(countries.pop()) #Pop Belgium
popItem.append(countries.pop(0)) #Pop Canada

countries.append("United Kingdom")
countries.remove("United Kingdom") #Only removes first occurrence

countries.sort() #sorted list
countries.reverse() #reverse order

print(len(countries)) #No of items in the list
print(countries) #print the entire list
