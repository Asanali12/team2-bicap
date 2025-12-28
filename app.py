from flask import Flask, jsonify
app = Flask(__name__)

data = {
    "Астана": {
        "SmallMart": [
            ("Хлеб", 280),
            ("Молоко", 250),
            ("Яйца", 720)
        ],
        "SuperFood": [
            ("Хлеб", 290),
            ("Молоко", 255),
            ("Яйца", 710)
        ]
    },
    "Кокшетау": {
        "Market24": [
            ("Хлеб", 260),
            ("Молоко", 240),
            ("Яйца", 690)
        ]
    },
    "Алматы": {
        "MegaStore": [
            ("Хлеб", 300),
            ("Молоко", 260),
            ("Яйца", 700)
        ],
        "DostykShop": [
            ("Хлеб", 310),
            ("Молоко", 270),
            ("Яйца", 730)
        ]
    }
}

def show_all():
    for city, shops in data.items():
        print(f"\n=== {city} ===")
        for shop, products in shops.items():
            print(f"\n  Магазин: {shop}")
            for name, price in products:
                print(f"    {name}: {price} тг")

def show_city():
    city = input("Город: ").strip().capitalize()
    if city not in data:
        print("Нет такого города!")
        return
    print(f"\n=== {city} ===")
    for shop, products in data[city].items():
        print(f"\n  Магазин: {shop}")
        for name, price in products:
            print(f"    {name}: {price} тг")

def add_shop():
    city = input("Город: ").strip().capitalize()
    if city not in data:
        print("Города нет!")
        return
    shop = input("Название магазина: ").strip()
    data[city][shop] = []
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



@app.route("/")
def hello():
    return "Hello World!"

@app.route("/products/<city>", methods=["GET"])
def get_products(city): # название города
    product_list = data[city]
    return jsonify(product_list)













if __name__ == "__main__":
    app.run(debug=True)
