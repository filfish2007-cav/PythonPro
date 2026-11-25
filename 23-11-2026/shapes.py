h = int(input("Введіть висоту h: "))
w = int(input("Введіть ширину w: "))

print("Прямокутник:")
for i in range(h):
    print("*" * w)

print("\nПрямокутний трикутник:")
for i in range(1, h + 1):
    print("*" * i)

print("\nПеревернутий трикутник:")
for i in range(h, 0, -1):
    print("*" * i)

print("\nФігура з порожниною:")
for i in range(h):
    if i == 0 or i == h - 1 or w < 2:
        print("*" * w)
    else:
        print("*" + " " * (w - 2) + "*")