meter = float(input("Enter  a value (1 meter) : "))
litr = float(input("Enter  a value (1 litr) : "))
f = meter * 3.28  # 1 метр = фут 3,28
d = meter * 39.37  # 1 метр = дюйм 39.37
mile = meter * 0.0006213  # 1метр = миля 0.0006213
pinta = litr * 2.11  # 1 литр = 2.11 американская пинта
gallon = litr * 0.26  # 1 Литр = 0,26 американский галлон
barrel = litr * 0.00628  # 1 литр  = 0.00628 американский баррель
print(f"Футы : {f} , Дюймы : {d} , Мили : {mile}")
print(f"Пинта : {pinta} , Галлон : {gallon} , Баррель : {barrel}")