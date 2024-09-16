# from numpy import*
# arr = array([
#                 [4, 6, 7],
#                 [7, 8, 9]
#             ])
# print(arr) #printing matrix form of an array



# from numpy import*
# arr = array([
#                 [4, 6, 7],
#                 [7, 8, 9]
#             ])
# print(arr.ndim) #ndim will give you the dimension of the arrays



# from numpy import*
# arr = array([
#                 [4, 6, 7],
#                 [7, 8, 9]
#             ])
# print(arr.shape) #.shape will give you the no. of columns and rows of the arrays and .size will give you the size of the columns and rows




# from numpy import*
# arr1 = array([
#                 [4, 6, 7],
#                 [7, 8, 9]
#             ])
# arr2 = arr1.flatten()
# print(arr2) #.flatten will flatten the 2 0r 3 dimentional array to just single dimentional




# from numpy import*
# arr1 = array([
#                 [4, 6, 7, 8, 9, 0],
#                 [7, 8, 9, 4, 6, 3]
#             ])
# arr2 = arr1.flatten()
# arr3 = arr2.reshape(2,2,3)
# print(arr3) #.reshape is a fuction to create 3 dimentional array from a single arrays




# from numpy import*
# arr = array([
#             [1,2,3,4],
#             [4,5,6,7]
#             ])
# m = matrix(arr) #matrix convert array into matrix.
# print(m)




# from numpy import*
# m = matrix ('1 2 3 4 ; 5 6 7 8')

# print(m) #you can as well use this shorter code to print matrix




# from numpy import*
# m = matrix ('1 2 ; 3 4 ; 5 6 ; 7 8')

# print(m) #semi colon placed in between the number of rows, demarcate the matrix to produce additional rows and columns




# from numpy import*
# m = matrix ('1 2 3 ; 4 5 6 ; 7 8 9')

# print(diagonal(m)) #use diagonal(matrix name) to print matrix diagonal




# from numpy import*
# m = matrix ('1 2 3 ; 4 5 6 ; 7 8 9')

# print(m.max()) #use m.min/max() to print minimum or maximum number in a matrix






# from numpy import*
# m1 = matrix ('1 2 3 ; 4 5 6 ; 7 8 9')
# m2 = matrix ('1 5 4 ; 2 6 6 ; 8 0 1')

# m3 = m1 / m2 #simply perform addition, subtraction and division of matrix using this format

# print(m3)



#Multiplication of matrix
fruits = ('apple', 'banana', 'orange')
print('original fruits', fruits)
fruits.append('cherry')
print('updated list', fruits)