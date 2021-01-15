boolean = True
i = 1
total = 0
priceDict = {}
print("Enter the item price to get the sum of prices. Press 'q' to get total")
while boolean:
    name = input(f"{i}. Item name : ")
    if name == "q":
        boolean = False
        break
    userInput = input(f"{i}. {name} price : ")
    try:
        total += int(userInput)
        print(f"Estimated Price : {total}\n")
        priceDict[name] = userInput
    except ValueError:
        print("Invalid Value: Please enter a number.")
    i += 1
print("\n ***Check the Prices List*** ")
i = 1
for key,value in priceDict.items():
    print(f"{i}. {key} price => {value}")
    i += 1
print("----------------------------")
print(f"The total sum is => {total}")