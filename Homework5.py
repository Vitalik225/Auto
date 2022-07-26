# number1 = int(input("Enter number : "))
# number2 = int(input("Enter number : "))
# number3 = int(input("Enter number : "))
# choose = input("Enter your chose \"add\" or \"multi\" :")
# if choose == "add":
#     print(f"{number1} + {number2} + {number3} = {number1 + number2 + number3}")
#
# elif choose == "multi":
#     print(f"{number1} * {number2} * {number3} = {number1 * number2 * number3}")
#
# else:
#     print("Error")

# # --------task2---------
number1 = int(input("Enter number : "))
number2 = int(input("Enter number : "))
number3 = int(input("Enter number : "))
choose = input("Enter your chose \"max\" or \"min\" or \"arif\" :")
if choose == "max":
    if number1 > number2:
        if number1 > number3:
            print(f"Max number :{number1}")
    if number2 > number1:
        if number2 > number3:
            print(f"Max number :{number2}")
    if number3 > number1:
        if number3 > number2:
            print(f"Max number :{number3}")
    if number1 == number2:
        if number1 == number3:
            print("Numbers equal")

elif choose == "min":
    if number1 < number2:
        if number1 < number3:
            print(f"Min number :{number1}")
    if number2 < number1:
        if number2 < number3:
            print(f"Min number :{number2}")
    if number3 < number1:
        if number3 < number2:
            print(f"Min number :{number3}")
    if number1 == number2:
        if number1 == number3:
            print("Numbers equal")

elif choose == "arif":
    print(f"({number1} + {number2} + {number3}) // 3 = {(number1 + number2 + number3) // 3}")

else:
    print("error")


# # -------------task3----------
# meter = float(input("Enter a value : "))
# choose = input("Enter your chose \"miles\" or \"yards\" or \"inches\" :")
# if choose == "miles":
#     print(f"{meter} * 0,000621371 = {meter * 0.000621371} miles")
# elif choose == "yards":
#     print(f"{meter} * 1,09361296 = {meter * 1.09361296} yards")
# elif choose == "inches":
#     print(f"{meter} * 39,37 = {meter * 39.37} inches")
# else:
#     print("Error!!!!"*4)
