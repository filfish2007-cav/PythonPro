amount = input("Введіть суму: ").replace(",", ".")
cents = round(float(amount) * 100)

values = [50000, 20000, 10000, 5000, 2000, 1000, 500,
          200, 100, 50, 20, 10, 5, 2, 1]

banknotes = 0
coins = 0
details = ""

for value in values:
    count = cents // value
    cents = cents % value

    if count > 0:
        details += f"{count} x {value / 100:g}\n"

        if value >= 500:
            banknotes += count
        else:
            coins += count

print(f"банкнот: {banknotes}")
print(f"монет: {coins}")
print("склад суми:")
print(details)