y = int(input("How Many Candies You Want?"))

i = 1
while i <= y:
    print ("Candy")
    i=i+1




av = 10

y = int(input("How Many Candies You Want?"))

i = 1
while i <= y:

    if i>av:
        print("Out of stock...")
        break

    print ("Candy")
    i=i+1

print("Bye!")




for i in range(1, 100):
    print (i)




for i in range(1, 100):

    if i%3==0 or i%5==0:
        continue

    print (i)

print("Bye!")





for i in range (1, 100):
    if(i%1!=0):
        pass
    else:
        print(i)

print("Bye")





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

