# 5. Write a Python program that takes two sets as input and returns a new set containing the elements that are in the first set but not in the second set, and the elements that are in the second set but not in the first set.

# # Q5
# A = {"Apple","Mango","Orage","Banana","Grapes","Guava"}
# B = {"Guava","Litchi","Papaya","Mango"}

# in_set_A = A - B
# print(in_set_A)

# in_set_B = B - A
# print(in_set_B)

# # Q5 (Second Method)
# A = {"Apple","Mango","Orage","Banana","Grapes","Guava"}
# B = {"Guava","Litchi","Papaya","Mango"}

# set_A = A.difference(B)
# print(set_A)

# set_B = B.difference(A)
# print(set_B)