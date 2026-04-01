""" sushi_orders = [
    {"name": "California Roll", "price": 8},
    {"name": "Spicy Tuna Roll", "price": 10},
    {"name": "Salmon Nigiri", "price": 6},
    {"name": "California Roll", "price": 8},
    {"name": "Dragon Roll", "price": 12},
    {"name": "Spicy Tuna Roll", "price": 10},
    {"name": "Miso Soup", "price": 4},
    {"name": "Edamame", "price": 5},
    {"name": "Salmon Nigiri", "price": 6},
    {"name": "California Roll", "price": 8}
]

def receipt(orders):
    the_receipt = {}
    for order in orders:
        if order["name"] in the_receipt:
            the_receipt[order["name"]]["qty"] +=1
        else:
            the_receipt[order["name"]] = {
                "price": order["price"],
                "qty": 1
            }
    for order, value in the_receipt.items():
        price = value["price"] * value["qty"]
        print(order, value["qty"], price)

receipt(sushi_orders) """

wards = {
    "Cardiology":  ["Alice", "Bob", "Carol"],
    "Neurology":   ["Diana", "Eve"],
    "Orthopedics": ["Frank", "Grace", "Hank"],
    "Oncology":    ["Ivy", "Bob"]
}

staff = {}
for dept, docs in wards.items():
    for doc in docs:
        if doc not in staff:
            staff[doc] = [dept]
        else:
            staff[doc].append(dept)
            
print(staff['Bob'])