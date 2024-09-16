# #adding a number to array
# from numpy import*
# arr = array([3,4,5,6,7,8])
# arr = arr + 5
# print(arr)




# #adding two arrays together
# from numpy import*
# arr1 = array([1,2,3,4,5,6])
# arr2 = array([5,4,3,2,6,4])
# arr3 = arr1 + arr2
# print(arr3)


# #Perform Mathematical operation in array
# from numpy import*
# arr1 = ([2,3,4,5,6,7,8,9])
# print(sum(arr1)) #repeat for cos, tan, log, sqrt, sum, min, max, sort



# #combining two arrays together
# from numpy import*
# arr1 = array([1,2,3,4,5,6])
# arr2 = array([5,4,3,2,6,4])
# print(concatenate([arr1,arr2]))





# #how to copy an array
# from numpy import*
# arr1 = array([0,9,8,7,6,5])
# arr2 = arr1
# print(arr1)
# print(arr2)

# print(id(arr1))
# print(id(arr2))






# #To create the same array with different address, we use .copy
# from numpy import*
# arr1 = ([2,5,8,0,4,7])
# arr2 = arr1.copy()
# print(arr1)
# print(arr2)

# print(id(arr1))
# print(id(arr2))





#For Deep copy
from numpy import*
arr1 = ([2,5,8,0,4,7])
arr2 = arr1.copy()
arr1[1] = 7
print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))