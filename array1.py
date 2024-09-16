#array syntax
from array import *
vals = array("i", [5, 9, -8, 4, 2])
print(vals)



# #Reverse in array
# from array import*
# vals = array("i", [5, -9, 4, 2])
# vals.reverse()
# print(vals)






# from array import*
# vals = array("i", [5, 9, 4, 2])
# vals.reverse()
# print(vals[2]) #single range are printed this way



# #For loop in array
# from array import *
# vals = array("i", [5, 9, 4, 7, 6, 9, 2])

# for i in range(7): #len(vals) in place of range "7"
#     print(vals[i])




# from array import*
# vals = array("i", [5, 9, 4, 2])

# for e in vals: #e can also be used in place of the i
#     print(e)



# #you can work with character
# from array import*
# vals = array("u", ['a', 'e', 'i', 'y'])
# for e in vals: 
#     print(e)



# New array in array
# from array import*
# vals = array("i", [5, 9, 4, 2])

# newa = array(vals.typecode, (a*a for a in vals))
# for e in newa: #e can also be used in place of the i
#     print(e)



# #While loop in array
# from array import*
# vals = array("i", [5, 9, 4, 2])

# newa = array(vals.typecode, (a*a*a for a in vals))


# i = 0

# while i<len(newa):
#     print(newa[i])
#     i+=1






# #Array values for user in Python
# from array import*
# arr = array('i', [])
# n = int(input("Enter the length of the array "))
# for i in range(n):
#     y = int(input("Enter the values "))
#     arr.append(y)

# print(arr)

# val = int(input("Enter the value for search "))
# k = 0
# for e in arr:
#     if e==val:
#         print(k)
#         break

#     k+=1

# print(arr.index(val))





# from array import*
# arr = array('characters', [])
# n = character(input("Enter the length of the array "))
# for characters in range(n):
#     y = character(input("Enter the values "))
#     arr.append(y)

# print(arr)