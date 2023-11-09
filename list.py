myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))

print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])

myFruitList[2] = "orange"
print(myFruitList)

x = input("Enter index: ")
xint = int(x)
print(type(xint))
print("Respective fruit: "+ myFruitList[xint])