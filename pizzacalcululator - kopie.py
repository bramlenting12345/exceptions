
print("...........................")
print("small pizza kost $ 5 ")
print("medium pizza kost $ 8 ")
print("large pizza kost $13 ")
print(".................................")

pizzasmall=input("hoeveel small pizza wil je ")
pizzamedium=input("hoeveel medium pizza wil je ")
pizzalarge=input("hoeveel large pizza wil je ")


try:
    pizzasmall = int(pizzasmall) 
    pizzamedium = int(pizzamedium)
    pizzalarge = int(pizzalarge)

except:
    print("Dat is geen optie kies het goeie antwoord")
    
else:


    prijssmall=(pizzasmall * 5)
    prijsmedium=(pizzamedium * 8)
    prijslarge=(pizzalarge * 13)

    print("de prijs is dan " + str(prijssmall + prijsmedium + prijslarge) + " euro")


