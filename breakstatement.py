for item in range (1,6):
    print(item)




for item in range (1, 6):
    if item == 3:
        break
    print(item)
print("The end")





while True:
    number = float(input("Enter a Number: "))
    if number < 0:
        break
    print("You entered: ", number)
    
print("The end!")





for i in range (5):
    number = float(input("Enter a Number: "))

    if number < 0:
        continue
    print(number)
print("The end")





for i in range (5):
    number = float(input("Enter a Number: "))

    if number < 0:
        break
    print(number)
print("The end")





languages = ("Python ", "Java ", "Swift ", "C ", "C++ ")
for character in languages:
    if character=="C++ " or character=="Swift ":
        continue 
    print(character)
print("The end")

