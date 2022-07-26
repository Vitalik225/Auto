# -------task1-----------
# number1 = input("Enter the digit : ")
# number2 = input("Enter the second digit : ")
# number3 = input("Enter the third digit : ")
# print(number1 + number2 + number3)

# # ------------task2---------
# number1 = int(input("Enter the digit : "))
# number2 = int(input("Enter the second digit : "))
# number3 = int(input("Enter the third digit : "))
# number4 = int(input("Enter the fourth digit : "))
# print(f"{number1} * {number2} * {number3} * {number4} = {number1 * number2 * number3 * number4}")

# #--------task3---------
# meter = float(input("Enter the number : "))
# print(f"Santimetr : {meter * 100} ")
# print(f"Decimeter : {meter * 10}")
# print(f"Millimeter : {meter * 1000}")
# print(f"Miles : {meter * 0.000621371}")

# # ------task4------------
# a = float(input("Enter base of a triangle :"))
# h = float(input("Enter height of triangle : "))
# print(f"Square of triangle = 0.5 * {a} * {h} = {0.5 * a * h}" )

#------task5----------
number = int(input("Enter 4  digits : "))
n1 = number // 1000
n2 = number % 1000 // 100
n3 = number % 100 // 10
n4 = number % 10
print(n4,n3,n2,n1)
