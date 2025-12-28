print("Магазин добавлен.")

def add_product():
    city = input("Город: ").strip().capitalize()
    if city not in data:
        print("Нет такого города!")
        return
    shop = input("Магазин: ").strip()
    if shop not in data[city]:
        print("Нет такого магазина!")
        return
    name = input("Название продукта: ").strip()
    price = int(input("Цена: "))
    data[city][shop].append((name, price))
    print("Продукт добавлен.")

while True:
    print("\n1 — Все данные")
    print("2 — По городу")
    print("3 — Добавить магазин")
    print("4 — Добавить продукт")
    print("0 — Выход")

    choice = input("> ")

    if choice == "1": show_all()
    elif choice == "2": show_city()
    elif choice == "3": add_shop()
    elif choice == "4": add_product()
    elif choice == "0":
        print("Выход...")
        break
    else:
        print("Неверный выбор")
