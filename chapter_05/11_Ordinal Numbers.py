numbers=list(range(1,10))
for number in numbers:
    if(number == 1):
        print(f"{number}st",end=" ", sep=" ")
    elif(number == 2):
        print(f"{number}nd",end=" ", sep=" ")
    elif(number == 3):
        print(f"{number}rd",end=" ", sep=" ")
    else:
        print(f"{number}th",end=" ", sep=" ")
        