def order(chicken):
    print(f"Order placed: your order is {chicken}")


def calculate_total(chicken):
    base_price = 25.5
    VAT = 0.15
    total_price = (base_price + len(chicken)) * (1 + VAT)
    return total_price


def get_order():
    print("Preparing order...")
    return "Collect your order"


myFood = input("What would you like? ")

order(myFood)

print(get_order())

order_total = calculate_total(myFood)
print(f"Your order cost: R{round(order_total, 2)}")